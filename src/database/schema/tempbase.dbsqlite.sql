--
-- File generated with SQLiteStudio v3.3.3 on Sat Sep 4 10:56:44 2021
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: settings
CREATE TABLE settings (settingName VARCHAR(64) PRIMARY KEY NOT NULL UNIQUE, settingValue TEXT NOT NULL, timeUpdated DATETIME NOT NULL);

CREATE TABLE temperature_event (
    temperatureReadingCelcius DOUBLE   NOT NULL,
    outcome                   INTEGER  NOT NULL,
    timeCreated               DATETIME NOT NULL
);

CREATE INDEX idx_temperature_event_outcome ON temperature_event (
    outcome
);

CREATE INDEX idx_temperature_event_reading ON temperature_event (
    temperatureReadingCelcius
);

CREATE INDEX idx_temperature_event_time_created ON temperature_event (
    timeCreated
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

