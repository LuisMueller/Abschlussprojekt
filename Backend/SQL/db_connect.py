import psycopg2
import os
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

# "SQL-Terminal“ in Python
cur = conn.cursor()

# SQL-Query definieren (alle Benutzer ausgeben)
query = 'SELECT * FROM users;'
cur.execute(query)

# Alle Ergebnisse holen
results = cur.fetchall()

# Zeilenweise ausgeben
print("Benutzerliste:")
for row in results:
    print(row)

# 🧹 Aufräumen
cur.close()
conn.close()
