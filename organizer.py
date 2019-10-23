import enum

class OrgType(enum.Enum):
	academic = 1
	volunteer = 2
	social = 3
	individual = 4

class Organizer:

	def __init__(self, name, org_type, request_id):
		self.name = name
		self.org_type = org_type
		self.request_id = request_id


	def display_info(self):
		print(self.name)
		print(self.org_type.name)
		print(self.request_id)