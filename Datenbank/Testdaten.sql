INSERT INTO public users (Name, Email)
VALUES (''Max Mustermann'', ''max@firma.de''),
       (''Anna Beispiel'', ''anna@firma.de''),
       (''Lisa Kraft'', ''lisa@firma.de'');

INSERT INTO "public"."users" (Name, Email)
VALUES ('Max Mustermann', 'max@firma.de'),
       ('Anna Beispiel', 'anna@firma.de'),
       ('Lisa Kraft', 'lisa@firma.de');

INSERT INTO vehicles (Model, Location, Seats, VehicleStatus)
VALUES (''5er BMW'', ''München'', 5, ''verfügbar''),
       (''1er BMW'', ''München'', 4, ''in_wartung''),
       (''Mercedes V-Klasse'', ''Berlin'', 7, ''verfügbar'');


INSERT INTO buchung(BookingStart, BookingEnd, Passanger, Destination, Reason, User_ID, Vehicles_ID)
VALUES (''2025 - 04 - 09 08:00:00'',
        ''2025 - 04 - 09 18:00:00'',
        3,
        ''Kundentermin Berlin'',
        ''Präsentation beim Kunden'',
        1, -- User_ID (Max Mustermann)
        3 -- Vehicle_ID (Mercedes V-Klasse)
       );




