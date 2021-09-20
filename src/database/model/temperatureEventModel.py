from .model import Model

class TemperatureEventModel(Model):

	def recordTemperature(self, temperature, wasPermittedEntry):
		timeStamp = self.currentTimestamp()
		self.query("INSERT INTO temperature_event(temperatureReadingCelcius, outcome, timeCreated) VALUES(?, ?, ?)",
			[temperature, 1 if wasPermittedEntry == True else 0, timeStamp])

	def countSuccessfulEntries(self):
		result = self.query("SELECT COUNT(*) AS c FROM temperature_event WHERE outcome = 1", [], True)
		if len(result) > 0:
			return int(result[0]["c"])

		return 0

	def getMostRecentTemperatures(self, max=100):
		return self.query("SELECT * FROM temperature_event ORDER BY timeCreated DESC LIMIT 0, ?", [max], True)
