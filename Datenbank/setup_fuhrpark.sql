-- ========== DROP TABLES IF EXISTS (für sauberen Neuanfang) ==========
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS vehicles;
DROP TABLE IF EXISTS users;

-- ========== 1. USERS ==========
CREATE TABLE users (
    User_ID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(150) UNIQUE NOT NULL
);

-- ========== 2. VEHICLES ==========
CREATE TABLE vehicles (
    Vehicle_ID SERIAL PRIMARY KEY,
    Model VARCHAR(100) NOT NULL,
    Location VARCHAR(100),
    Seats INT CHECK (Seats > 0),
    VehicleStatus VARCHAR(20) DEFAULT 'verfügbar' CHECK (
        VehicleStatus IN ('verfügbar', 'gebucht', 'in_wartung', 'defekt')
    )
);

-- ========== 3. BOOKINGS ==========
CREATE TABLE bookings (
    Booking_ID SERIAL PRIMARY KEY,
    BookingStart TIMESTAMP NOT NULL,
    BookingEnd TIMESTAMP NOT NULL,
    Passanger INT CHECK (Passanger > 0),
    Destination VARCHAR(100),
    Reason VARCHAR(200),

    User_ID INT,
    Vehicles_ID INT,

    CONSTRAINT fk_user FOREIGN KEY (User_ID) REFERENCES users(User_ID) ON DELETE CASCADE,
    CONSTRAINT fk_vehicle FOREIGN KEY (Vehicles_ID) REFERENCES vehicles(Vehicle_ID) ON DELETE SET NULL,

    CHECK (BookingEnd > BookingStart)
);

-- ========== INSERT INTO USERS ==========
INSERT INTO users (Name, Email)
VALUES
  ('Max Mustermann', 'max@firma.de'),
  ('Anna Beispiel', 'anna@firma.de'),
  ('Lisa Kraft', 'lisa@firma.de');

-- ========== INSERT INTO VEHICLES ==========
INSERT INTO vehicles (Model, Location, Seats, VehicleStatus)
VALUES
    (''5er BMW'', ''München'', 5, ''verfügbar''),
    (''1er BMW'', ''München'', 4, ''in_wartung''),
    (''Mercedes V-Klasse'', ''Berlin'', 7, ''verfügbar'');

-- ========== INSERT INTO BOOKINGS ==========
INSERT INTO bookings (BookingStart, BookingEnd, Passanger, Destination, Reason, User_ID, Vehicles_ID)
VALUES (
  '2025-04-09 08:00:00',
  '2025-04-09 18:00:00',
  3,
  'Kundentermin Berlin',
  'Präsentation beim Kunden',
  1,
  1
);

-- ========== SELECTS ZUM TESTEN ==========
-- Alle Benutzer anzeigen
SELECT * FROM users;

-- Fahrzeuge anzeigen (alle)
SELECT * FROM vehicles;

-- Nur verfügbare Fahrzeuge
SELECT * FROM vehicles WHERE VehicleStatus = 'verfügbar';

-- Alle Buchungen
SELECT * FROM buchung;

-- Alle Buchungen + Nutzer + Fahrzeug (JOIN)
SELECT
    b.Booking_ID,
    u.Name AS Benutzer,
    v.Model AS Fahrzeug,
    b.BookingStart,
    b.BookingEnd,
    b.Destination
FROM buchung b
JOIN users u ON b.User_ID = u.User_ID
JOIN vehicles v ON b.Vehicles_ID = v.Vehicle_ID;
