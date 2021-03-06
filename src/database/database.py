import sqlite3
import os

schemaPath = os.path.dirname(os.path.realpath(__file__)) + "/schema/tempbase.dbsqlite.sql"
dbPath = os.path.dirname(os.path.realpath(__file__)) + "/tempbase.db"

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class Database:

	def __init__(self, dbFp):
		self.dbFp = dbFp
		self.exists = False
		if os.path.isfile(dbFp):
			self.exists = True

		self.connection = sqlite3.connect(dbFp)
		self.connection.row_factory = dict_factory
		self.cursor = self.connection.cursor()

	def autoSetup(self):
		if self.exists:
			return

		with open(schemaPath, "r") as fh:
			for transaction in fh.read().split(";"):
				self.connection.execute(transaction)

ActiveDatabase = Database(dbPath)
ActiveDatabase.autoSetup()