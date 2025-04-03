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
CREATE TABLE Bookings (
    BookingID SERIAL PRIMARY KEY,
    UserID INT NOT NULL,
    VehicleID INT NOT NULL,
    BookingStart TIMESTAMP NOT NULL,
    BookingEnd TIMESTAMP NOT NULL,
    Passengers INT NOT NULL,
    Destination VARCHAR(200) NOT NULL,
    Reason TEXT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE
);
