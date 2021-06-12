import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import QTimer

class Scene(QWidget):
	def __init__(self, x=600, y=400, speed=33, title="My Game"):
		super().__init__()

		self.setGeometry(50,50,x,y)
		self.setWindowTitle(title)

    self.width = x
    self.height = y


		self.speed = speed

		self.timer = QTimer()
		self.timer.timeout.connect(self.updateTask)

	def start(self):
		self.timer.start(self.speed)
		
	def stop(self):
		self.timer.stop()		

	def paintEvent(self, event):
		self.updateGame()	
		
	# This should be overridden by your game
	def updateTask(self):
		self.update()		