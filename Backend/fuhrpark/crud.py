import psycopg2
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "../../properties.env")
load_dotenv(dotenv_path)
load_dotenv("properties.env")

def buche_fahrzeug(user_id, vehicle_id, start, end, destination, reason):
    if start >= end:
        return False, "Startzeitpunkt muss vor dem Endzeitpunkt liegen"
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

        # 1. Zeitüberschneidung prüfen suchstart
        cur.execute("""
                    SELECT 1 FROM buchung
                    WHERE
                        vehicles_id = %(vid)s
                    AND (
                            (%(start)s >= bookingstart AND %(end)s <= bookingend)
                        OR 
                            (%(start)s <= bookingend AND %(start)s >= bookingstart)
                        OR
                            (%(end)s >= bookingstart AND %(end)s <= bookingend)
                        OR 
                            (%(start)s <= bookingstart And %(end)s >= bookingend)
                    );
                """, {'vid': vehicle_id, 'start': start, 'end': end})
        conflicts = cur.fetchall()

        if conflicts:
            return False, "Fahrzeug ist im gewünschten Zeitraum bereits gebucht."

        # 2. Fahrzeug existiert? (optional, kannst du lassen)
        cur.execute("SELECT vehicle_id FROM vehicles WHERE vehicle_id = %s AND vehiclestatus != 'in_wartung';", (vehicle_id,))
        if not cur.fetchone():
            return False, "Fahrzeug-ID nicht gefunden oder Fahrzeug in Wartung."

        # 3. Buchung einfügen
        cur.execute("""
                    INSERT INTO buchung (BookingStart, BookingEnd, Passenger, Destination, Reason, User_ID, Vehicles_ID)
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                """, (
            start,
            end,
            1,  # Standard: 1 Passagier
            destination,
            reason,
            user_id,
            vehicle_id
        ))

        conn.commit()

        return True, "Buchung erfolgreich eingetragen."

    except Exception as e:
        return False, f"Fehler bei der Buchung: {e}"

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

#GET all buchungen Fnktion

def get_all_buchungen():
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORT")
        )
        cur = conn.cursor()

        cur.execute("""
            SELECT booking_id, user_id, vehicles_id, bookingstart, bookingend, passenger, destination, reason
            FROM buchung
            ORDER BY bookingstart ASC;
        """)
        rows = cur.fetchall()

        buchungen = []
        for row in rows:
            buchungen.append({
                "booking_id": row[0],
                "user_id": row[1],
                "vehicle_id": row[2],
                "bookingstart": row[3],
                "bookingend": row[4],
                "passenger": row[5],
                "destination": row[6],
                "reason": row[7]
            })

        return buchungen

    except Exception as e:
        return []

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def get_filtered_buchungen(
        user_id=None,
        vehicle_id=None,
        start=None,
        end=None,
        limit=None,
        offset=None,
        sort_by="bookingstart",
        order="asc"

):
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORT")
        )
        cur = conn.cursor()

        base_query = """
            SELECT booking_id, user_id, vehicles_id, bookingstart, bookingend, passenger, destination, reason
            FROM buchung
        """
        filters = []
        params = {}

        if user_id is not None:
            filters.append("user_id = %(uid)s")
            params['uid'] = user_id

        if vehicle_id is not None:
            filters.append("vehicles_id = %(vid)s")
            params['vid'] = vehicle_id

        if start is not None and end is not None:
            filters.append("""
            (
                        (%(start)s >= bookingstart AND %(end)s <= bookingend)
                    OR 
                        (%(start)s <= bookingend AND %(start)s >= bookingstart)
                    OR
                        (%(end)s >= bookingstart AND %(end)s <= bookingend)
                    OR 
                        (%(start)s <= bookingstart And %(end)s >= bookingend)
            )
            """)
            params['start'] = start
            params['end'] = end

        if filters:
            base_query += " WHERE " + " AND ".join(filters)

        # Sortierung
        if sort_by not in ["bookingstart", "bookingend", "user_id", "vehicles_id"]:
            sort_by = "bookingstart"
        order = "DESC" if order.lower() == "desc" else "ASC"
        base_query += f" ORDER BY {sort_by} {order}"

        # Pagination
        if limit:
            base_query += " LIMIT %(limit)s"
            params['limit'] = limit
        if offset:
            base_query += " OFFSET %(offset)s"
            params['offset'] = offset
        #Test
        print("QUERY:", base_query)
        print("PARAMS:", params)

        cur.execute(base_query, params)
        rows = cur.fetchall()

        return [
            {
                "booking_id": row[0],
                "user_id": row[1],
                "vehicle_id": row[2],
                "bookingstart": row[3],
                "bookingend": row[4],
                "passenger": row[5],
                "destination": row[6],
                "reason": row[7],
            }
            for row in rows
        ]

    except Exception as e:
        print("Fehler bei der Buchungsabfrage:", e)
        return []

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def update_buchung(booking_id: int, update_data: dict):
    conn = None
    cur = None

    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORT")
        )
        cur = conn.cursor()

        fields = []
        values = []

        for key, value in update_data.items():
            if value is not None:
                fields.append(f"{key} = %s")
                values.append(value)

        if not fields:
            return False, "Keine Daten zum Aktualisieren übergeben."

        query = f"""
            UPDATE buchung
            SET {", ".join(fields)}
            WHERE booking_id = %s
        """
        values.append(booking_id)
        cur.execute(query, tuple(values))
        conn.commit()

        return True, "Buchung erfolgreich aktualisiert."

    except Exception as e:
        return False, f"Fehler beim Aktualisieren: {e}"

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def delete_buchung(booking_id: int):
    conn = None
    cur = None

    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORT")
        )
        cur = conn.cursor()

        cur.execute("DELETE FROM buchung WHERE booking_id = %s;", (booking_id,))
        if cur.rowcount == 0:
            return False, "Keine Buchung mit dieser ID gefunden."

        conn.commit()
        return True, "Buchung erfolgreich gelöscht."

    except Exception as e:
        return False, f"Fehler beim Löschen: {e}"

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

