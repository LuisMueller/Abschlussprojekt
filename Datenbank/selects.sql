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