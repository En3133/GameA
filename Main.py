from GameA.Scene import Scene
from GameA.Sprite import Sprite
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


# Sean's Sprite Sheet
# https://opengameart.org/content/cat-fighter-sprite-sheet
# Cat by DogChicken @ OpenGameArt.org














