from model import settingsModel
from model import temperatureEventModel

settings = settingsModel.SettingsModel(True)
value = settings.get("version")
if value == None:
	print("No value found, creating...")
	settings.set("version", "1.0")
else:
	print(value)

event = temperatureEventModel.TemperatureEventModel(True)
event.recordTemperature(36, True)
event.recordTemperature(40, False)

print(event.getMostRecentTemperatures())