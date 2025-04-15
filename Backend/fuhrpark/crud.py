import psycopg2
import os
from dotenv import load_dotenv

load_dotenv("properties.env")

def buche_fahrzeug(user_id, vehicle_id, start, end):
    conn = None
    cur = None

    try:
        # Verbindung zur Datenbank herstellen
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORT")
        )
        cur = conn.cursor()

        # 1. Fahrzeugstatus prüfen
        cur.execute("SELECT VehicleStatus FROM vehicles WHERE Vehicle_ID = %s;", (vehicle_id,))
        result = cur.fetchone()

        if not result:
            return False, "Fahrzeug-ID nicht gefunden."

        if result[0] != "verfügbar":
            return False, f"Fahrzeug ist aktuell nicht verfügbar. Status: {result[0]}"

        # 2. Zeitüberschneidung prüfen
        cur.execute("""
            SELECT * FROM buchung
            WHERE Vehicles_ID = %s
              AND BookingStart < %s
              AND BookingEnd > %s;
        """, (vehicle_id, end, start))
        conflicts = cur.fetchall()

        if conflicts:
            return False, "Fahrzeug ist im gewünschten Zeitraum bereits gebucht."

        # 3. Buchung einfügen
        cur.execute("""
            INSERT INTO buchung (BookingStart, BookingEnd, Passanger, Destination, Reason, User_ID, Vehicles_ID)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """, (
            start,
            end,
            1,                  # Standard: 1 Passagier
            "Ziel wird später ergänzt",  # Platzhalter
            "Grund wird später ergänzt", # Platzhalter
            user_id,
            vehicle_id
        ))

        # 4. Fahrzeugstatus updaten
        cur.execute("UPDATE vehicles SET VehicleStatus = 'gebucht' WHERE Vehicle_ID = %s;", (vehicle_id,))
        conn.commit()

        return True, "Buchung erfolgreich eingetragen."

    except Exception as e:
        return False, f"Fehler bei der Buchung: {e}"

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
