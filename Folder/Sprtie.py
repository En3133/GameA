import sys
from PyQt5.QtGui import QImage, QPainter


class Sprite():
	def __init__(self, thisScene, imageFile, xSize, ySize):
		self.width=xSize
		self.height=ySize
		self.animation = False
		self.scene = thisScene
		self.x = 0
		self.y = 0		
		
		# Load our file
		self.file = QImage(imageFile)
	
	def update(self, offX = 0, offY = 0):
		self.draw(offX, offY)
		
	def draw(self, offX, offY): 
		drawX	= self.x - int(self.width/2) - offX
		drawY = self.y - int(self.height/2) - offY		
		qp = QPainter(self.scene)
		qp.drawImage(drawX, drawY, self.file, )