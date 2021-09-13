class FsmState:

	def __init__(self, fsm):
		self.identifier = "__unique__identifier__"
		self.label = "__STATE_LABEL__"
		self.fsm = fsm

	def onEnterState(self, args=None):
		pass

	def onExitState(self):
		pass

	def main(self):
		pass