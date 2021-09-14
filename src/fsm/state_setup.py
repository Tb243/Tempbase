from fsm.state import FsmState
from web.http_server import HttpServer
from web.wss_server import WSServer
import os

class StateSetup(FsmState):

	def __init__(self, fsm):
		self.identifier = "setup"
		self.label = "Setup"
		self.fsm = fsm
		self.httpServer = HttpServer("0.0.0.0", 5000, os.path.dirname(os.path.realpath(__file__)) + "/../web/front/build")
		self.wsServer = WSServer("0.0.0.0", 8080)
		self.fsm.addStateHook(self.onStateChange)
		self.httpServer.openBrowser()

	def onStateChange(self, state, stateData):
		self.wsServer.broadcast({
			"state": state,
			"stateData": stateData
		})

	def main(self):
		#Set up server
		#Set up database
		#Set up web browser (launch web browser)
		self.fsm.transitionState("waitForHand")