import enum

class RoomType(enum.Enum):
	lecture = 1
	seminar = 2
	lab = 3
	meeting = 4
	office = 5

class Room:

	def __init__(self, number, capacity, room_types):
		self.number = number
		self.capacity = capacity
		self.room_types = room_types
		self.occupied = False
		self.events = []

	def create_event():
		pass

	def display_events(self):
		for event in self.events:
			print(event)

	def update_event():
		pass

	def delete_event():
		