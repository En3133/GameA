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

		# assign scene width to self.cWidth
    self.cwidth = self.scene.width

		# assign scene height to self.cHeight	
    self.cheight = self.scene.height

		
		# Load our file
		self.file = QImage(imageFile)

		self.boundAction = 0
	
	def update(self, offX = 0, offY = 0):
		self.checkBounds()
		
		self.draw(offX, offY)

		def move(self):
      pass 

	def draw(self, offX, offY): 
		drawX	= self.x - int(self.width/2) - offX
		drawY = self.y - int(self.height/2) - offY		
		qp = QPainter(self.scene)
		qp.drawImage(drawX, drawY, self.file, )

  def checkBounds(self):
    leftBorder = 0
    rightBorder = self.cwidth
    topBorder = 0
    downBorder = self.cheight



