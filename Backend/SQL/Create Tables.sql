-- Tabelle für Benutzer
CREATE TABLE Users (
    UserID SERIAL PRIMARY KEY,   
    Name VARCHAR(50) NOT NULL,
    Email VARCHAR(100)
);

-- Tabelle für Fahrzeuge
CREATE TABLE Vehicles (
    VehicleID SERIAL PRIMARY KEY, 
    Model VARCHAR(50) NOT NULL,
    Location VARCHAR(75) NOT NULL
);

-- Tabelle für Buchungen
CREATE TABLE buchung (
    Booking_ID SERIAL PRIMARY KEY,
    BookingStart TIMESTAMP NOT NULL,
    BookingEnd TIMESTAMP NOT NULL,
    Passenger INT CHECK (Passenger > 0),
    Destination VARCHAR(100),
    Reason VARCHAR(200),

    User_ID INT,
    Vehicles_ID INT,

    CONSTRAINT fk_user FOREIGN KEY (User_ID) REFERENCES users(User_ID) ON DELETE CASCADE,
    CONSTRAINT fk_vehicle FOREIGN KEY (Vehicles_ID) REFERENCES vehicles(Vehicle_ID) ON DELETE SET NULL,

    CHECK (BookingEnd > BookingStart)
);
