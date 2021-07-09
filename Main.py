from Game.Scene import Scene
from Game.Sprite import Sprite
from Game.Background import Background
from Game.Block import Block
from Game.Keys import *
import sys
from PyQt5.QtWidgets import QApplication
from Ground import Ground
from enum import Enum

app = QApplication(sys.argv)

class States(Enum):
	FALLING = 0
	WALK = 1
	JUMP = 2
	STAND = 3

class Facing(Enum):
	RIGHT = 0
	LEFT = 1

class Character(Sprite):
	def __init__(self, thisScene, sprite, x, y):
		self.state = States.FALLING
		self.facing = Facing.RIGHT
		super().__init__(thisScene, sprite, x, y)
		self.stateTimer = 0
		self.dy = 7 
		
	def update(self):
		if self.state == States.FALLING:
			if self.scene.ground.collidesWith(self):
				self.y = self.scene.ground.y - (self.height/2 + self.scene.ground.height / 2)
				self.standBehavior
		elif self.state == States.STAND or self.state == States.WALK:
			if self.scene.keyDown[Scene.K_SPACE]:
				self.jumpBehavior
		elif self.state == States.STAND:
			if self.scene.keysDown[Scene.K_RIGHT] or self.scene.keysDown[Scene.K_LEFT]:
				self.walkBehavior
		elif self.state == States.WALK:
			if (self.facing == Facing.RIGHT) and (self.scene.keysDown[Scene.K_RIGHT] != True):
				self.standBehavior
			if (self.facing == Facing.LEFT) and (self.scene.keysDown[Scene.K_LEFT] != True):
				self.standBehavior
		elif self.state == States.JUMP:
			self.stateTimer -= 1
			if self.stateTimer < 1:
				self.dy = self.dy * -1
				self.state = States.FALLING
		super().update()

	def standBehavior(self):
		self.dy = 0
		self.dx = 0
		self.state = States.STAND
		self.pauseAnimation()

	# override this in your Character
	def jumpBehavior(self):
		pass

	# override this in your Character
	def walkBehavior(self):
		pass


# change the numbers of your sprite's iniit to your sprite sheet
# add the loadAnimation, generateAnimationCycles, setAnimationspeed, and playAnimation methods
class Ian(Character):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/oct.PNG", 100, 100)
		self.x = 90
		self.y = 100

		# add loadAnimation, generateAnimation, setAnimationSpeed, and playAnimation methods
		# super().__init__(thisScene, "filename.png", sheetX, sheetY)
		# loadAnimation(sheetX, sheetY, cellX, cellY)
		#self.loadAnimation(500, 200, 100, 100)
		#self.generateAnimationCycles()
		#self.setAnimationSpeed(100)	# 10 times a second / ms
		#self.playAnimation()
		
		self.dx = 10
		self.dy = -4		
		self.boundAction = Scene.WRAP
		#self.state = Character.runLeft


	def update(self):
		super().update()

	# Add a method called walkBehavior. 
	# This should check if self.scene.keysDown[K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and 10
	# If not check if self.scene.keysDown[K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and -10
#	def walkBehavior(self):
#		if self.scene.keysDown[K_RIGHT]:
#			self.facing = Facing.RIGHT
#			self.setCurrentCycle(Facing.RIGHT)
#			self.startAnimation()
#			self.dx = 4
#		elif self.scene.keysDown[K_LEFT]:
#			self.facing = Facing.LEFT
#			self.setCurrentCycle(Facing.LEFT)
#			self.startAnimation()
#			self.dx = -4

	# Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.
	#def jumpBehavior(self):
#		self.stateTimer = 50
#		self.dy = -5			





class Arthur(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene,"sprites/spider.png",100,100)
    self.x = 90
    self.y = 100

		# add loadAnimation, generateAnimation, setAnimationSpeed, and playAnimation methods
		# super().__init__(thisScene, "filename.png", sheetX, sheetY)
		# loadAnimation(sheetX, sheetY, cellX, cellY)
		#self.loadAnimation(500, 200, 100, 100)
		#self.generateAnimationCycles()
		#self.setAnimationSpeed(100)	# 10 times a second / ms
		#self.playAnimation()
		
    self.dx = 10
    self.dy = -4
    self.boundAction = Scene.WRAP
	  #self.state = Character.runLeft

  def update(self):
     super().update()

	


class Iris(sprite):
  def __init__(self, thisScene):
    super()._init_(thisScence, "sprites/oct.PNG", 100, 100)
    self.x = 50
    self.y = 100
    self.dx = 1
    self.dy = 2
    print("iris")



class Amy(sprite):
  def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/oct.PNG", 100, 100)
    self.x = 50
    self.y = 100
    self.dy = -1
    print("amy")

class Tyrone(sprite):
  def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/spider.PNG", 100, 100)
    self.x = 40
    self.x = 50
    self.dx = 3
    print("Tyrone")


    
class Kelly(sprite):
   def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/oct.PNG", 100,100)
    self.x = 250
    self.y = 120     
    self.dx = -2
    self.dy = -1
    print("Kelly")




# Sheet 256 x 58
# Cell: 32 x 29
# super().__init__(thisScene, "yourimage.png", sheetX, sheetY)
# loadAnimation(sheetX, sheetY, CellX, cellY)



  # Add a method called walkBehavior. 
  # This should check if self.scene.keysDown[K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and 10
  # If not check if self.scene.keysDown[K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and -10
    
  # Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.



# sheet: 	715 x 474
# Cell : 143 x 237
# super().__init__(thisScene, "yourimage.png", sheetX, sheetY)
# loadAnimation(sheetX, sheetY, CellX, cellY)
'''
class Johnny(Character):
	def __init__(self,thisScene):
		super().__init__(thisScene,"sprites/johnny_sprite.png", 715, 474)#COPYRIGHT anthony: YEEET
		self.x = 100
		self.y = 900
		self.dx = 1
		self.dy = 1
		print("Johnny")
	self.loadAnimation(715, 474, 143, 237)
		self.generateAnimationCycles()
		self.setAnimationSpeed(100)	
		self.playAnimation()

	def update(self):
			super().update()
	def walkBehavior(self):
		if self.scene.keysDown[K_RIGHT]:
			sdfdsself.facing = Facing.RIGHT
			sfsdef.setCurrentCycle(Facing.RIGHT)
			sel.sdfsd()
			sfsdfsddssdsdfsdsdlf.dy = 1
		elif self.fds.keysDown[K_LEFT]:
			selt.facfsdfsfding = Facing.LEFT
			slololfdsfsd.setCurrentCycle(Facing.LEFT)
			surf.fdssfsdtfffsdsddsartAnimation
			self.fsddy = -99
	def jdsumpBfsfehavior(self):
		ssdelf.stafsdteTimer = 50
		sefdsflf.dx = -99	

	# Add a method called walkBehavior. 
  # This should check if self.scene.keysDown[K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and 10
  # If not check if self.scene.keysDown[K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and -10
    
  # Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.

	
# Sheet: 165 x 60
# Cell: 41 x 30
# super().__init__(thisScene, "yourimage.png", sheetX, sheetY)
# loadAnimation(sheetX, sheetY, CellX, cellY)
'''
class Game(Scene):
	def __init__(self):
    super().__init__(600,600)
		self.bg0 = Background(self, "sprites/parallax-forest-back-trees.png", 1020, 600, .25, 0)
		self.bg1 = Background(self, "sprites/parallax-forest-middle-trees.png", 1020, 600, .5, 0)		
		self.bg2 = Background(self, "sprites/parallax-forest-front-trees.png", 1020, 600, .75, 0)
		self.bg3 = Background(self, "sprites/parallax-forest-lights.png", 1020, 600, 1, 0)		
		self.ground = Ground(self)
    
		self.ian = Ian(self)
    self.arthur = Arthur(self)


    
	def updateGame(self):
		self.bg0.update()
		self.bg1.update()
		self.bg2.update()
		self.bg3.update()
		self.ground.update()

		# player sprites
		self.ian.update()
    self.arthur.update()


	

myGame = Game()
myGame.start()
myGame.show()
sys.exit(app.exec_())



'''

from Game.Scene import Scene
from Game.Sprite import Sprite
from Game.Background import Background
from Game.Block import Block
import sys
from PyQt5.QtWidgets import QApplication

from Ground import Ground

app = QApplication(sys.argv)


class Ian(Sprite):
  def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/oct.PNG", 100, 100)
    self.x = 100
    self.y = 400
    self.dx = 2
    self.dy = 1
    print("ian")
    def update(self):
      if self.y > 600:
        self.y = 600;
           
      super.update()
  
  
class Arthur(Sprite):
  def __init__(self):
    super().__init__(thisScene, "sprites/somedude.jpg", 100, 100)
    self.x = 50
    self.y = 100
    self.dx = -1 
    def update(self):
      if self.y > 600 and self.x > 200:
        self.y = 600;
           
      super.update()
     

class Iris(sprite):
  def __init__(self, thisScence):
    super()._init_(thisScence, "sprites/oct.PNG", 100, 100)
    self.x = 50
    self.y = 100
    self.dx = 1
    self.dy = 2
    print("iris")
    print(self.__bases__)


class Amy(sprite):
  def __init__(self):
    super().__init__(thisScene, "sprites/oct.PNG", 100, 100)
     self.x = 50
     self.y = 100
     self.dy = -1
     print("amy")
     print(self.__bases__)

class Tyrone(sprite):
def_innit_(self, thisScene)
  super().__init__(thisScene, "sprites/spider.PNG", 100, 100)
  self.x = 40
  self.x = 50
  self.dx = 3
  print("Tyrone")


    
class Kelly(sprite):
  def__init__(sprite
    super().__init__(thisScene, "sprites/oct.PNG", 100,100)
    self.x = 250
    self.y = 120     
    self.dx = -2
    self.dy = -1



class Game(Scene):
	def __init__(self):
		super().__init__(600,600)
    self.bg0 = Background(self, "sprites/parallax-forest-back-trees.png", 1020, 600, .25, 0)
		self.bg1 = Background(self, "sprites/parallax-forest-middle-trees.png", 1020, 600, .5, 0)		
		self.bg2 = Background(self, "sprites/parallax-forest-front-trees.png", 1020, 600, .75, 0)
		self.bg3 = Background(self, "sprites/parallax-forest-lights.png", 1020, 600, 1, 0)	

		self.ground = Ground(self)


    self.ian = Ian(self)
    self.ian.object = "something"
    del self.ian.object
    self.iris = Iris(self)
    self.kelly = Kelly(self)
    self.amy = Amy(self)

    

	def updateGame(self):
    	self.bg0.update()
		  self.bg1.update()
		  self.bg2.update()
		  self.bg3.update()
		  self.ground.update()

      self.ian.update()
      self.iris.update()
      self.amy.update()
      self.kelly.update()





myGame = Game()
myGame.start()
myGame.show()
sys.exit(app.exec_())







'''