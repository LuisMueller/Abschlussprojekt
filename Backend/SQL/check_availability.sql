-- Zeitliche Verfügbarkeitsprüfung für ein bestimmtes Fahrzeug

SELECT * FROM buchung
WHERE Vehicles_ID = 3
  AND BookingStart < '2025-04-09 13:00:00'
  AND BookingEnd > '2025-04-09 09:00:00';

-- Alle Fahrzeuge, die im gewünschten Zeitraum verfügbar sind

SELECT * FROM vehicles
WHERE Vehicle_ID NOT IN (
    SELECT Vehicles_ID FROM buchung
    WHERE BookingStart < '2025-04-09 13:00:00'
      AND BookingEnd > '2025-04-09 09:00:00'
)
AND VehicleStatus = 'verfügbar';
