from database import ActiveDatabase
from datetime import datetime

class Model:

	def __init__(self, debug=False):
		self.debug = debug

	def query(self, query, args, fetch=False):
		if self.debug:
			print(query)

		ActiveDatabase.cursor.execute(query, args)
		ActiveDatabase.connection.commit()
		if fetch:
			return ActiveDatabase.cursor.fetchall()
		return None

	def currentTimestamp(self):
		return datetime.today().strftime("%Y-%m-%d-%H:%M:%S")