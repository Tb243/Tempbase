from model import settingsModel

settings = settingsModel.SettingsModel(True)
value = settings.get("version")
if value == None:
	print("No value found, creating...")
	settings.set("version", "1.0")
else:
	print(value)