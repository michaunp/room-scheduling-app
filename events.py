

class Event:

	#initializes objects of the class
	# handles the creation of an event
	def __init__(self, name, start, end, roomNum, eventType):
		self.name = name
		self.start = start
		self.end = end
		self.roomNum = roomNum
		self.eventType = eventType

	#methods - Create Read Update Delete

	def CreateEvent(name, start, end, roomNum, eventType):
