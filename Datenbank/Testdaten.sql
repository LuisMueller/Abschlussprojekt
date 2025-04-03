-- Benutzer hinzufügen
INSERT INTO Users (Name, Email) VALUES ('Max Mustermann', 'max@example.com');

-- Fahrzeuge hinzufügen
INSERT INTO Vehicles (Model, Location) 
VALUES ('VW Golf', 'Garage 1'), 
       ('BMW 3 Series', 'Garage 2');

-- Buchung hinzufügen
INSERT INTO Bookings (UserID, VehicleID, BookingStart, BookingEnd, Passengers, Destination, Reason)
VALUES (1, 1, '2024-11-21 08:00:00', '2024-11-21 12:00:00', 3, 'Frankfurt', 'Meeting mit Kunden');
