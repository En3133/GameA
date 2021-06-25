from SimpleGame.Scene import Scene
from SimpleGame.Sprite import Sprite
import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)



class Game(Scene):
	def __init__(self):
		super().__init__(600,600)
    self.ian = Ian(self)
    self.iris = Iris(self)
    self.kelly = Kelly(self)
    self.amy = Amy(self)

    

	def updateGame(self):
      self.ian.update()
      self.iris.update()
      self.amy.update()
      self.kelly.update()

myGame = Game()
myGame.start()
myGame.show()
sys.exit(app.exec_())


class Ian(sprite):
  def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/oct.PNG", 100, 100)
     self.x = 100
     self.y = 400
     self.dx 2
     self.dy -1
  
  
class Arthur(sprite):
  def __init__(self):
    super().__init__(thisScene, "sprites/arthur_sprite.png", 100, 100)
     self.x = 50
     self.y = 100
     self.dx = -1 
     

class Iris(sprite):
  def __init__(self, thisScence):
    super()._init_(thisScence,
    "sprites/iris_sprite.png", 100, 100)
    self.x = 50
    self.y = 100
    self.dx = 1
    self.dy = 2


class Amy(sprite):
  def __init__(self):
    super().__init__(thisScene, "sprites/amy_sprite.png", 100, 100)
      self.x = 50
      self.y = 100
      self.dy = -1

class Tyrone(sprite):
def_innit_(self, thisScene)
  super().__init__(thisScene, "sprites/tryone_sprite.png", 100, 100)

      self.x = 40
      self.x = 50
      self.dx = 3

class Kelly(sprite):
  def__init__(sprite
    super().__init__(thisScene, "sprites/kelly_sprite.png", 100,100)
     self.x = 250
     self.y = 120     
    self.dx = -2
    self.dy = -1





















