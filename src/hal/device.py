class Device:

	def __init__(self):
		self.name = "__BASE_CLASS__"
		self.isVirtual = False

	def validateConfig(self):
		raise NotImplementedError()

	def setup(self):
		raise NotImplementedError()

	def destroy(self):
		raise NotImplementedError()

	def read(self):
		raise NotImplementedError()