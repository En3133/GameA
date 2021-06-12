from SimpleGame.Scene import Scene
from SimpleGame.Sprite import Sprite
import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)



class Game(Scene):
	def __init__(self):
		super().__init__(600,600)
		self.spaceship = Sprite(self, "spaceship100.png", 100, 93)
		self.spaceship.y=200


		self.spaceship.dx=1
		
	def updateGame(self):
		print("My Update")
		self.spaceship.x +=1
		
		# paint sprites
		self.spaceship.update()

myGame = Game()
myGame.start()
myGame.show()
sys.exit(app.exec_())


class Ian(sprite):
  def __init__(self):
    super.__init__()
    self.x = 100
    self.y = 200
  def move(self):
    self.x += 1


class kelly(sprite):
  def __init__(self):
    super.__init__()
    self.x 
  def move(self):
    self.y += 2















