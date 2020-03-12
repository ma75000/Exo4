class Task:
	def __init__(self, subject, dateCreation):
		self.subject = subject
		self.isDone = False
		self.dateCreation = dateCreation 

	def markItDone(self):
		self.isDone = True

	def __str__(self):
		return f"{self.subject}"