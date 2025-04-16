import psycopg2
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "../../properties.env")
load_dotenv(dotenv_path)
load_dotenv("properties.env")

def buche_fahrzeug(user_id, vehicle_id, start, end):
    if start >= end:
        return Flase, "Startzeitpunkt muss vor dem Endzeitpunkt liegen"
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

        # 1. Zeitüberschneidung prüfen
        cur.execute("""
                    SELECT 1 FROM buchung
                    WHERE vehicles_id = %s
                      AND bookingstart < %s
                      AND bookingend > %s;
                """, (vehicle_id, end, start))
        conflicts = cur.fetchall()

        if conflicts:
            return False, "Fahrzeug ist im gewünschten Zeitraum bereits gebucht."

        # 2. Fahrzeug existiert? (optional, kannst du lassen)
        cur.execute("SELECT vehicle_id FROM vehicles WHERE vehicle_id = %s;", (vehicle_id,))
        if not cur.fetchone():
            return False, "Fahrzeug-ID nicht gefunden."

        # 3. Buchung einfügen
        cur.execute("""
                    INSERT INTO buchung (BookingStart, BookingEnd, Passanger, Destination, Reason, User_ID, Vehicles_ID)
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                """, (
            start,
            end,
            1,  # Standard: 1 Passagier
            "Ziel wird später ergänzt",
            "Grund wird später ergänzt",
            user_id,
            vehicle_id
        ))

        # 4. Kein Status-Update mehr nötig
        conn.commit()

        return True, "Buchung erfolgreich eingetragen."

    except Exception as e:
        return False, f"Fehler bei der Buchung: {e}"

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
