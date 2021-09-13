--
-- File generated with SQLiteStudio v3.3.3 on Sat Sep 4 10:56:44 2021
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: settings
CREATE TABLE settings (settingName VARCHAR(64) PRIMARY KEY NOT NULL UNIQUE, settingValue TEXT NOT NULL, timeUpdated DATETIME NOT NULL);

-- Table: temperature_event
CREATE TABLE temperature_event (userIdentifier VARCHAR(128), temperatureReadingCelcius DOUBLE NOT NULL, distanceFromSensorCm DOUBLE NOT NULL, outcome INTEGER NOT NULL, timeCreated DATETIME NOT NULL);

-- Index: idx_temperature_event_outcome
CREATE INDEX idx_temperature_event_outcome ON temperature_event (outcome);

-- Index: idx_temperature_event_reading
CREATE INDEX idx_temperature_event_reading ON temperature_event (temperatureReadingCelcius);

-- Index: idx_temperature_event_sensor
CREATE INDEX idx_temperature_event_sensor ON temperature_event (distanceFromSensorCm);

-- Index: idx_temperature_event_time_created
CREATE INDEX idx_temperature_event_time_created ON temperature_event (timeCreated);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

