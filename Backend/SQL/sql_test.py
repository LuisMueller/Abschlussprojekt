import psycopg2
import os
from datetime import datetime
from dotenv import load_dotenv

#env-Datei laden
dotenv_path = os.path.join(os.path.dirname(__file__), "../../properties.env")
load_dotenv(dotenv_path)
load_dotenv("properties.env")

# Properties.env auslesen
DB_USER = os.getenv("DB_USER")
DB_PASSWORT = os.getenv("DB_PASSWORT")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")

# Verbindung zur PostgreSQL-Datenbank herstellen
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORT
)

cur = conn.cursor()

# Beispielwerte für Verfügbarkeitsprüfung
vehicle_id = 3
start = '2025-04-09 09:00:00'
end = '2025-04-09 13:00:00'

# Fahrzeugstatus checken
cur.execute("""
    SELECT VehicleStatus FROM vehicles
    WHERE Vehicle_ID = %s;
""", (vehicle_id,))
status_result = cur.fetchone()

if not status_result:
    print("Fahrzeug nicht gefunden.")
elif status_result[0] != 'verfügbar':
    print(f"Fahrzeug ist aktuell nicht verfügbar – Status: {status_result[0]}")
else:
    # nach überbuchungen checken
    cur.execute("""
        SELECT * FROM buchung
        WHERE Vehicles_ID = %s
          AND BookingStart < %s
          AND BookingEnd > %s;
    """, (vehicle_id, end, start))
    conflict = cur.fetchall()

    if conflict:
        print("Fahrzeug ist im gewünschten Zeitraum bereits gebucht.")
        for row in conflict:
            print("Konflikt:", row)
    else:
        print("Fahrzeug ist verfügbar!")

# 🧹 Aufräumen
cur.close()
conn.close()
