import psycopg2
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "../properties.env")
load_dotenv(dotenv_path)
load_dotenv("properties.env")

def buche_fahrzeug(user_id, vehicle_id, start, end):
    conn = None
    cur = None
    try:
        # Verbindung aufbauen
        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_HOST = os.getenv("DB_HOST")
        DB_NAME = os.getenv("DB_NAME")
        DB_PORT = os.getenv("DB_PORT")

        # Verbindung zur PostgreSQL-Datenbank herstellen
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cur = conn.cursor()

        #Fahrzeugstatus prüfen
        cur.execute("SELECT VehicleStatus FROM vehicles WHERE Vehicle_ID = %s;", (vehicle_id,))
        result = cur.fetchone()

        if not result:
            return "Fahrzeug-ID nicht gefunden."

        if result[0] != "verfügbar":
            return f"Fahrzeug ist nicht verfügbar. Aktueller Status: {result[0]}"

        # Schritt 2: Zeitüberschneidung prüfen
        cur.execute("""
            SELECT * FROM buchung
            WHERE Vehicles_ID = %s
              AND BookingStart < %s
              AND BookingEnd > %s;
        """, (vehicle_id, end, start))
        conflicts = cur.fetchall()

        if conflicts:
            return "Fahrzeug ist im gewünschten Zeitraum bereits gebucht."

        # Schritt 3: Buchung einfügen
        cur.execute("""
            INSERT INTO buchung (BookingStart, BookingEnd, Passanger, Destination, Reason, User_ID, Vehicles_ID)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """, (
            start,
            end,
            1,  # Standard: 1 Passagier
            "Testziel",
            "Testbuchung",
            user_id,
            vehicle_id
        ))

        # Schritt 4: Fahrzeugstatus auf 'gebucht' setzen
        cur.execute("UPDATE vehicles SET VehicleStatus = 'gebucht' WHERE Vehicle_ID = %s;", (vehicle_id,))

        conn.commit()
        return "Buchung erfolgreich angelegt!"

    except Exception as e:
        return f"Fehler bei der Buchung: {e}"

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    # Beispielwerte zum Testen
    user_id = 1
    vehicle_id = 1
    start = "2025-04-10 09:00:00"
    end = "2025-04-10 13:00:00"

    result = buche_fahrzeug(user_id, vehicle_id, start, end)
    print(result)  # <- Das hier fehlt dir wahrscheinlich
