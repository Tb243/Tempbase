import json
import os

filePath = os.path.dirname(os.path.realpath(__file__)) + "/config.json"

if not os.path.exists(filePath):
	print("Fatal error: No config.json file exists. You must create one. See config.example.json in src/ for example.")
	exit(1)

with open(filePath, "r") as fh:
	config = json.loads(fh.read())
