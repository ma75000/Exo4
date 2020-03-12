from datetime import datetime

class TaskList:
	def __init__(self):
		self.listTask = list()

	def addTask(self, task):
		self.listTask.append(task)

	def remove(self, task):
		self.listTask.remove(task)

	def display(self):
		for task in self.listTask:
			print(self.listTask)