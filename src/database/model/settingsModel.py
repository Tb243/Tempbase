from .model import Model

class SettingsModel(Model):

	def get(self, settingName, defaultValue = None):
		results = self.query("SELECT * FROM settings WHERE settingName = ?", [settingName], True)
		if len(results) < 1:
			return defaultValue

		return results[0]["settingValue"]

	def set(self, settingName, value):
		timeStamp = self.currentTimestamp()
		if self.get(settingName):
			self.query("UPDATE settings SET settingValue = ?, timeUpdated = ? WHERE settingName = ?", [value, timeStamp, settingName])
		else:
			self.query("INSERT INTO settings VALUES (?, ?, ?)", [settingName, value, timeStamp])