import logging
from websocket_server import WebsocketServer
import threading
import json
import time

class WSServer:

	def __init__(self, bind, port):
		self.bind = bind
		self.port = port
		
		self.server = None
		self.serverThread = threading.Thread(target=self.setup, daemon=True)
		self.serverThread.start()

	def setup(self):
		self.server = WebsocketServer(self.port, host=self.bind, loglevel=logging.INFO)
		self.server.set_fn_new_client(self.newClient)
		self.server.run_forever()

	def broadcast(self, jsonData):
		print("Broadcasting...")
		print(json.dumps(jsonData))
		self.server.send_message_to_all(json.dumps(jsonData))

	def newClient(self, client, server):
		print("A new client has connected!")
		print(client)

if __name__ == "__main__":
	server = WSServer("0.0.0.0", 8080)
	while True:
		time.sleep(1)