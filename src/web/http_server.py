import http.server
import socketserver
import threading
import os
import time
import atexit
import webbrowser

class HttpServer:

	def __init__(self, bind, port, webRoot):
		self.bind = bind
		self.port = port
		self.webRoot = webRoot
		os.chdir(webRoot)

		self.httpd = None
		self.serverThread = threading.Thread(target=self.setup, daemon=True)
		self.serverThread.start()

	def setup(self):
		with socketserver.TCPServer((self.bind, self.port), http.server.SimpleHTTPRequestHandler) as httpd:
			print("HTTP server running on http://%s:%s, serving from %s" % (self.bind, self.port, self.webRoot))
			self.httpd = httpd
			atexit.register(self.onExit)
			httpd.serve_forever()

	def onExit(self):
		if self.httpd:
			print("Shutting down HTTP server")
			self.httpd.shutdown()

	def openBrowser(self):
		webbrowser.open("http://localhost:5000/", 2)

if __name__ == "__main__":
	server = HttpServer("0.0.0.0", 5000, os.path.dirname(os.path.realpath(__file__)) + "/public/dist")
	while True:
		time.sleep(1)