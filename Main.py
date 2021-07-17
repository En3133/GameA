from Game.Scene import Scene
from Game.Sprite import Sprite
from Game.Background import Background
from Game.Block import Block
from Game.Keys import *
import sys
from PyQt5.QtWidgets import QApplication
from Ground import Ground
from enum import Enum
import random

app = QApplication(sys.argv)

class States(Enum):
	FALLING = 0
	WALK = 1
	JUMP = 2
	STAND = 3

class Facing(Enum):
	RIGHT = 0
	LEFT = 1

class Camera():
	def __init__(self, thisScene):
		self.viewWidth = Scene.width
		self.viewHeight = Scene.height
		self.scene = thisScene

	def follow(self, sprite):
		self.sprite = sprite

	def update(self):
		if self.sprite.drawX < 250:
			if self.sprite.x < 300:
				self.sprite.x = 300
			else:
				self.scene.offsetX -= 6
		if self.sprite.drawX > (350):
			if self.sprite.x > (26*120):
				self.sprite.x = (26*120)
			else:
				self.scene.offsetX += 6
			

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


class Spaceship(Sprite):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/spaceship100.png", 100, 100)
		self.x = 300
		self.y = 100
		self.dx = 6
		self.timer = 60
		self.enemies = []
	def checkBounds(self):

		if self.drawX < 0:
			self.dx = 6
		if self.drawX > 550:
			self.dx = -6
		self.timer -= 1
		if self.timer < 1:
			self.timer = 60
			self.enemySpawn()

		for enemy in self.enemies:
			enemy.update(self.scene.offsetX, self.scene.offsetY)

	def enemySpawn(self):
		temp = random.randint(0,2)
		newEnemy = 0
		if temp == 0:
			newEnemy = Enemy(self.scene, self.x, self.y)
		elif temp==1:
			newEnemy = GroundEnemy(self.scene, self.x, self.y)
		elif temp ==2:
			newEnemy = FlyingEnemy(self.scene, self.x, self.y)
		self.enemies.append(newEnemy)
		
class BaseEnemy(Sprite):
	def __init__(self, thisScene, file, width, height, x, y):
		super().__init__(thisScene, file, width, height)
		self.setBoundAction(Scene.DIE)
		self.x = x
		self.y = y
		self.dy = 3
		self.timer = 120
	def update(self, offsetX, offsetY):
		self.timer -= 1
		if self.timer < 1:
			self.makeDecision()
		super().update(offsetX, offsetY)
	def makeDecision(self):
		pass		

class Enemy(BaseEnemy):
	def __init__(self, thisScene, x, y):
		super().__init__(thisScene, "sprites/egg3.png", 128, 128, x, y)
	def update(self, offsetX, offsetY):
		super().update(offsetX, offsetY)
	def makeDecision(self):
		self.dy = 3

class GroundEnemy(BaseEnemy):
	def __init__(self, thisScene, x, y):
		super().__init__(thisScene, "sprites/egg3.png", 128, 128, x, y)
	def update(self, offsetX, offsetY):
		super().update(offsetX, offsetY)
	def makeDecision(self):
		self.dy = 3

class FlyingEnemy(BaseEnemy):
	def __init__(self, thisScene, x, y):
		super().__init__(thisScene, "sprites/birb.png", 100, 73, x, y)
		self.dy = 0
	def update(self, offsetX, offsetY):
		super().update(offsetX, offsetY)
	def makeDecision(self):
		self.timer = 30
		decision = random.randint(0,1)		
		# if the decision is random
		if decision == 0:
			self.dx = random.randint(-5, 5)
			self.dy = random.randint(-5, 5)
		# home in on main character
		if decision == 1:
			# find out if the main character is to the left of the enemy
			if self.scene.ian.x < self.x:
				movementX = -1
			# find out if the main character is to the right of the enemy - justin
			if self.scene.ian.x > self.x:
				movementX = 1

			# find out if the main character is underneath the enemy (hint check y)- lucas
			if self.scene.ian.y < self.y:
				movementY = -1
			# find out if the main character is above of the enemy - johnny
			if self.scene.ian.y > self.y:
				movementY = 1

			# move at random speed
			self.dx = (random.randint(0,5) * movementX)
			self.dy = (random.randint(0,5) * movementY)





# change the numbers of your sprite's iniit to your sprite sheet
# add the loadAnimation, generateAnimationCycles, setAnimationspeed, and playAnimation methods
class Ian(Character):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/ghost_thing.png", 500, 200)
		self.x = 100
		self.y = 20
		self.dx = 10
		self.dy = 1
    #self.loadAnimation(520, 200, 100, 100)
    #self.gneerateAnimationCycles()
    #self.setAnimationSpeed(30)
		self.boundAction = Scene.WRAP
		#self.state = Character.runLeft
	def update(self):

		super().update()



class Arthur(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene,"sprites/rockperson.png",100,100)
    self.x = 90
    self.y = 100
    self.dx = 20
    self.dy = 4
  def update(self):
     super().update()

	

class Yon(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene,"sprites/dog_running.png",100,100)
    self.x = 10
    self.y = 20
    self.dx = 0
    self.dy = 5
  def update(self):
     super().update()





class Iris(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/oct.PNG", 100, 100)
    self.x = 50
    self.y = 100
    self.dx = 1
    self.dy = 2
    print("iris")



class Amy(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/sean_sprite.png", 100, 100)
    self.x = 50
    self.y = 100
    self.dy = 2
    print("amy")

class Tyrone(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/warrior.png", 100, 100)
    self.x = 40
    self.x = 50
    self.dx = 3
    print("Tyrone")


    
class Kelly(Character):
   def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/nija.PNG", 100,100)
    self.x = 250
    self.y = 120     
    self.dx = -2
    self.dy = 2
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
    self.iris = Iris(self)
    self.tyrone = Tyrone(self)
    self.kelly = Kelly(self)
    self.amy = Amy(self)

  def updateGame(self):
    self.bg0.update()
    self.bg1.update()
    self.bg2.update()
    self.bg3.update()
    self.ground.update()

		# player sprites
    self.ian.update()
    self.arthur.update()
    self.iris.update()
    self.tyrone.update()
    self.kelly.update()
    self.amy.update()


	

myGame = Game()
myGame.start()
myGame.show()
sys.exit(app.exec_())



'''





class --------(Character):
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