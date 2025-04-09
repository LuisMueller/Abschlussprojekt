import os
import psycopg2

from dotenv import load_dotenv

load_dotenv("properties.env")


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")

conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

print("Verbindung hergestellt")

cur = conn.cursor()

query = 'SELECT * FROM users;'
cur.execute(query)

results = cur.fetchall()

for row in results:
    print(row)

cur.close()
conn.close()
