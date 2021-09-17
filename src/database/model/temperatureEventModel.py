from .model import Model

class TemperatureEventModel(Model):

	def recordTemperature(self, temperature, wasPermittedEntry):
		timeStamp = self.currentTimestamp()
		self.query("INSERT INTO temperature_event(temperatureReadingCelcius, outcome, timeCreated) VALUES(?, ?, ?)",
			[temperature, 1 if wasPermittedEntry == True else 0, timeStamp])

	def getMostRecentTemperatures(self, max=100):
		return self.query("SELECT * FROM temperature_event ORDER BY timeCreated DESC LIMIT 0, ?", [max], True)
