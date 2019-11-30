class Building:
	def __init__(self, name, address, rooms):
		self.name = name
		self.address = address
		self.rooms = []

	def DisplayRooms(self):
		for room in self.rooms:
			print room

	def RemoveRoom(self, room):
		for curr_room in self.rooms:
			if room == curr_room:
				self.remove(room)

	#TODO: add Update method!