from datetime import datetime
import unittest
from exo4.TaskList import TaskList
from exo4.Task import Task

class TestTask(unittest.TestCase):
	def test_taskListAdd(self):
		taskListWitness = [
			Task("test1", datetime.strptime("10/11/2010", "%d/%m/%Y")), 
			Task("test2", datetime.strptime("09/11/2010", "%d/%m/%Y"))
		]
		taskListTest = TaskList()
		taskListTest.addTask(
			Task("test1", datetime.strptime("10/11/2010", "%d/%m/%Y"))
		)
		taskListTest.addTask(
			Task("test2", datetime.strptime("09/11/2010", "%d/%m/%Y"))
		)
		self.assertEqual(taskListTest.listTask, taskListWitness)

	def test_taskCreation(self):
		pass

	def test_taskDelete(self):
		pass

	def test_taskMarkItDone(self):
		pass

	def taskDisplay(self):
		pass

if __name__ == '__main__':
    unittest.main()