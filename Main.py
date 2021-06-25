import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)

window = QWidget()

window.setGeometry(50,50,320,200)
window.setWindowTitle("PyQT5 Example")

#Sean's Label
seanLabel = QLabel(window)
seanLabel.setText("Hi, Sean here!")
seanLabel.move(110,85)

#Alex
alexLabel = QLabel(window)
alexLabel.setText("Tony The Ant Means Anthony.")
alexLabel.move(100,80)

#Anthony
tonyLabel = QLabel(window)
tonyLabel.setText("Yeet")
tonyLabel.move(185, 70)

#Justin
justinLabel = QLabel(window)
justinLabel.setText("I like apples")
justinLabel.move(150, 75)

#Quingyun
qingyunLabel = QLabel(window)
qingyunLabel.setText("Heloo")
qingyunLabel.move(165,65)




window.show()

sys.exit(app.exec_())



'''from Game.Scene import Scene
from Game.Sprite import Sprite
import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)





# class Anthony 205, 194

# 34x39
class Justin(Sprite):
  def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/justin_sprite.png", 34, 39)
    self.x = 50
    self.y = 20
    self.dx = 2
    self.dy = -2
  def update(self):
    if self.y > 100:
      self.y = 200
      self.dy = 1
    super().update()
    

class Sean(Sprite):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/sean_sprite.png", 49, 55)
		self.x = 100
		self.y = 100
		self.dy = 1
		print("Sean")
	def update(self):
		if self.y > 500:
			self.y = 500
			self.dy = 0
		super().update()
	

# 1558,942		
class Johnny(Sprite):
	def __init__(self,thisScene):
		super().__init__(thisScene,"sprites/johnny_sprite.png", 1558, 942)
		self.x = 100
		self.y = 900
		self.dx = 1
		self.dy = 1
		print("Johnny")
	def update(self):
		if self.y > 500:
			self.y = 500
			self.dy = 0
		super().update()

	
#40x29
class Siqi(Sprite):
    def __init__(self,thisScene):
        super().__init__(thisScene,"sprites/siqi_sprite.png",240, 174)
        self.x=-100
        self.y=-150
        self.dx=2
        self.dy=3
        print("Siqi")
    def update(self):
      if self.y > 500:
        self.y = 500
        self.dy = 0
      super().update()
        
class Alex(Sprite):
    def __init__(self,thisScene):
        super().__init__(thisScene, "sprites/alex_sprite.png", 81, 102)
        self.x = 110
        self.y = 90
        self.dx=2
        self.dy=3
        print("Alex")
    def update(self):
      if self.y  > 500:
        self.y = 500
        self.dy = 0
      super().update()

# 50 x 50
class Qingyun(Sprite):
    def __init__(self, thisScene):
        super().__init__(thisScene, "sprites/qingyun_sprite.png", 200, 50)	#make sure to pass thisScene, the path to your image, and the size
        self.x = 200
        self.y = 50
        self.dx = 5
        self.dy = 5
    def update(self):
        if self.y > 500:
          self.y = 500
          self.dy = 0
        super().update()
    


# 42x30
class Lucas(Sprite):
	def __init__(self,thisScene):
		super().__init__(thisScene,"sprites/lucas_sprite.png", 42,30)
		self.x += 75
		self.y += 75
		self.x=-100
		self.y=-150
		self.dx=10
		self.dy=10

class Anthony(Sprite):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/anthony_sprite.png", 205, 194)
		self.x = 200
		self.y = 500
		self.dx = 1
		self.dy = 1
		print("Anthony")
	def update(self):
		if self.y > 500
		   self.y = 500
		   self.dy = 0
		   super().update()
		


			




# Sean's Sprite Sheet
# https://opengameart.org/content/cat-fighter-sprite-sheet
# Cat by DogChicken @ OpenGameArt.org

#Lucas' sprite sheet
#https://opengameart.org/content/esquire-animated-classic-hero-edit
#Knight by Umz @http://umzgames.com/
#villan: https://opengameart.org/content/monster-green
#by PiXeRaT @ OpenGameArt.org

#Siqi's sprite sheet - needs sprite sheet
#https://opengameart.org/content/ninja-animated----hero
#https://opengameart.org/content/explosion-sheet

#https://opengameart.org/content/skull-monster-sprite-sheet

#Qingyun's sprite sheet
#https://opengameart.org/content/cute-monster-sprite-sheet(hero)
#https://opengameart.org/content/skull-monster-sprite-sheet(villain)
#Hero + Villian by DogChicken

# Anthony's sprite sheet
# https://opengameart.org/content/dog-platformer-fighter
# No attribution needed

#
# Justin's sprite sheet
# https://opengameart.org/content/pixel-art-mini-golem

#By PixElthen



# Alex's sprite sheet
# https://opengameart.org/content/dude-with-arms
# by Iwan Gabovitch



#Johnny's sprite sheet
#https://opengameart.org/content/cartoon-rogue --villain
#By laetissima
#https://opengameart.org/content/skeleton-warrior-2
#by sonild



class Game(Scene):
	def __init__(self):
		super().__init__(600,600)
		self.sean = Sean(self)
		self.sean.boomerang = "Test"
		del self.sean.boomerang
		self.johnny = Johnny(self)
		self.siqi = Siqi(self)
		self.alex = Alex(self)
		self.justin = Justin(self)
		self.qingyun = Qingyun(self)
		self.lucas = Lucas(self)
		self.anthony = Anthony(self)

	
    
	def updateGame(self):
		self.sean.update()
		self.siqi.update()
		self.johnny.update()
		self.alex.update()
		self.lucas.update()
		self.qingyun.update()
		self.justin.update()
		self.anthony.update()

myGame = Game()
myGame.start()
myGame.show()
sys.exit(app.exec_())





	



















			




# Sean's Sprite Sheet
# https://opengameart.org/content/cat-fighter-sprite-sheet
# Cat by DogChicken @ OpenGameArt.org

#Lucas' sprite sheet
#https://opengameart.org/content/esquire-animated-classic-hero-edit
#Knight by Umz @http://umzgames.com/
#villan: https://opengameart.org/content/monster-green
#by PiXeRaT @ OpenGameArt.org

#Siqi's sprite sheet - needs sprite sheet
#https://opengameart.org/content/ninja-animated----hero
#https://opengameart.org/content/explosion-sheet

#https://opengameart.org/content/skull-monster-sprite-sheet

#Qingyun's sprite sheet
#https://opengameart.org/content/cute-monster-sprite-sheet(hero)
#https://opengameart.org/content/skull-monster-sprite-sheet(villain)
#Hero + Villian by DogChicken

# Anthony's sprite sheet
# https://opengameart.org/content/dog-platformer-fighter
# No attribution needed

#
# Justin's sprite sheet
# https://opengameart.org/content/pixel-art-mini-golem

#By PixElthen



# Alex's sprite sheet
# https://opengameart.org/content/dude-with-arms
# by Iwan Gabovitch



#Johnny's sprite sheet
#https://opengameart.org/content/cartoon-rogue --villain
#By laetissima
#https://opengameart.org/content/skeleton-warrior-2
#by sonild



class Game(Scene):
	def __init__(self):
		super().__init__(600,600)
		self.sean = Sean(self)
		self.sean.boomerang = "Test"
		del self.sean.boomerang
		self.johnny = Johnny(self)
		self.siqi = Siqi(self)
		self.alex = Alex(self)
		self.justin = Justin(self)
		self.qingyun = Qingyun(self)
		self.lucas = Lucas(self)
		self.anthony = Anthony(self)

	
    
	def updateGame(self):
		self.sean.update()
		self.siqi.update()
		self.johnny.update()
		self.alex.update()
		self.lucas.update()
		self.qingyun.update()
		self.justin.update()
		self.anthony.update()

myGame = Game()
myGame.start()
myGame.show()
sys.exit(app.exec_())























"""from SimpleGame.Scene import Scene
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


"""




