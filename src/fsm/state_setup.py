from fsm.state import FsmState
from web.http_server import HttpServer
import os

class StateSetup(FsmState):

	def __init__(self, fsm):
		self.identifier = "setup"
		self.label = "Setup"
		self.fsm = fsm
		self.httpServer = HttpServer("0.0.0.0", 5000, os.path.dirname(os.path.realpath(__file__)) + "/../web/front/build")
		self.httpServer.openBrowser()

	def main(self):
		#Set up server
		#Set up database
		#Set up web browser (launch web browser)
		self.fsm.transitionState("waitForHand")