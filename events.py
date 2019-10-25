import enum

class EventType:
	def __init__(enum.Enum):
		social = 1
		profDev = 2
		academic = 3
		career = 4
		volunteer = 5

class Event:

	#initializes objects of the class
	# handles the creation of an event
	def __init__(self, name, start, end, roomNum, eventType):
		self.name = name
		self.start = start
		self.end = end
		self.roomNum = roomNum
		self.eventType = eventType

	#CRUD methods
	#TODO: need Update Method!

	def PrintEvent(self):
		print(self.name)
		print(self.start)
		print(self.end)
		print(self.roomNum)
		print(self.eventType)
