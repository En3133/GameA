from Game.Scene import Scene
from Game.Sprite import Sprite
from Game.Background import Background
from Game.Block import Block
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
			if (self.facing == facing.RIGHT) and (self.scene.keysDown[Scene.K_RIGHT] != True):
				self.standBehavior
			if (self.facing == facing.LEFT) and (self.scene.keysDown[Scene.K_LEFT] != True):
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
		super().__init__(thisScene, "sprites/oct.PNG", 500, 200)
		self.x = 90
		self.y = 100




		# add loadAnimation, generateAnimation, setAnimationSpeed, and playAnimation methods
		# super().__init__(thisScene, "filename.png", sheetX, sheetY)
		# loadAnimation(sheetX, sheetY, cellX, cellY)
		self.loadAnimation(500, 200, 100, 100)
		self.generateAnimationCycles()
		self.setAnimationSpeed(100)	# 10 times a second / ms
		self.playAnimation()
		
		self.dx = 1
		self.dy = 1		
		self.boundAction = Scene.WRAP
		self.state = Character.runLeft


	def update(self):
		super().update()

	# Add a method called walkBehavior. 
	# This should check if self.scene.keysDown[K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and 10
	# If not check if self.scene.keysDown[K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and -10
	def walkBehavior(self):
		if self.scene.keysDown[K_RIGHT]:
			self.facing = Facing.RIGHT
			self.setCurrentCycle(Facing.RIGHT)
			self.startAnimation()
			self.dx = 4
		elif self.scene.keysDown[K_LEFT]:
			self.facing = Facing.LEFT
			self.setCurrentCycle(Facing.LEFT)
			self.startAnimation()
			self.dx = -4

	# Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.
	def jumpBehavior(self):
		self.stateTimer = 50
		self.dy = -5			




# Sheet 256 x 58
# Cell: 32 x 29
# super().__init__(thisScene, "yourimage.png", sheetX, sheetY)
# loadAnimation(sheetX, sheetY, CellX, cellY)

class Justin(Character):
    def __init__(self, thisScene):
        super().__init__(thisScene, "sprites/spider.png", 100, 100)
        self.x = 100
        self.y = 100
        self.dx = 2
        self.dy = 2
    print("Justin")
    def update(self):
        super().update()
    def walkBehavior(self):
		if self.scene.keysDown[K_RIGHT]:
			self.facing = Facing.RIGHT
			self.setCurrentCycle(Facing.RIGHT)
			self.startAnimation()
			self.dx = 3
		elif self.scene.keysDown[K_LEFT]:
			self.facing = Facing.LEFT
			self.setCurrentCycle(Facing.LEFT)
			self.startAnimation()
			self.dx = 3
		self.loadAnimation(500, 500, 100, 100)
		self.generateAnimationCycles()
		self.setAnimationSpeed(100)
		self.playAnimation()
    

  # Add a method called walkBehavior. 
  # This should check if self.scene.keysDown[K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and 10
  # If not check if self.scene.keysDown[K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and -10
    
  # Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.



# sheet: 	715 x 474
# Cell : 143 x 237
# super().__init__(thisScene, "yourimage.png", sheetX, sheetY)
# loadAnimation(sheetX, sheetY, CellX, cellY)
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
class Siqi(Character):
    def __init__(self,thisScene):
        super().__init__(thisScene, "siqi_sprite.png",165,60) 
        self.x=-100
        self.y=-150
        self.dx=2
        self.dy=3
        print("Siqi")
    self.loadAnimation(165, 60, 41, 30)
		self.generateAnimationCycles()
		self.setAnimationSpeed(100)	
		self.playAnimation()
	def update(self):
		super().update()
    def walkBehavior(self):
		if self.scene.keysDown[K_RIGHT]:
			self.facing = Facing.RIGHT
			self.setCurrentCycle(Facing.RIGHT)
			self.startAnimation()
			self.dx = 6
		elif self.scene.keysDown[K_LEFT]:
			self.facing = Facing.LEFT
			self.setCurrentCycle(Facing.LEFT)
			self.startAnimation(
			self.dx = -6
    def jumpBehavior(self):
		self.stateTimer = 50
		self.dy = -5	

	  # Add a method called walkBehavior. 
    # This should check if self.scene.keysDown[K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and 10
    # If not check if self.scene.keysDown[K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and -10
    
    # Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.
        

# Sheet: 162 x 204
# Cell: 81 x 102
class Alex(Character):
    def __init__(self,thisScene):
        super().__init__(thisScene, "sprites/alex_sprite.png", 100, 102)
        self.x = 110
        self.y = 90
        self.dx=2
        self.dy=3
        print("Alex")
    def update(self):
      super().update()

      self.loadAnimation(500,200,100,100)
      self.generateAnimationCycles()
      self.setAnimationspeed(100)
      self.playAnimation()
		# Add a method called walkBehavior. 
    # This should check if self.scene.keysDown[K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and 10
    def walkBehavior(self):
      if self.scene.keysDown[K_RIGHT]:
        self.facing = Facing.RIGHT
        self.setCurrentCycle(Facing.Right)
        self.startAnimation()
        self.dx = -5
      elif self.scene.keysDown[K_LEFT]
        self.facing = Facing.LEFT
        self.setCurrentCycle(Facing.Left)
        self.startAnimation()
        self.dx = -5

    def jumpBehavior(self)
      self.stateTimer = 60
      self.dy = -6  
      
         
    # If not check if self.scene.keysDown[K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and -10
    
    # Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.

# 50 x 50
# Sheet: 315x110
# Cell: 63x55
class Qingyun(Character):
    def __init__(self, thisScene):
        super().__init__(thisScene, "sprites/qingyun_sprite.png", 315, 110)	#make sure to pass thisScene, the path to your image, and the size
        self.x = 200
        self.y = 50
        self.dx = 5
        self.dy = 5
        print("Qingyun")
    def update(self):
      super().update()
      self.loadAnimation(500, 200, 100, 100)
		self.generateAnimationCycles()
		self.setAnimationSpeed(100)
		self.playAnimation()
		
		self.dx = 1
		self.dy = 1		
		self.boundAction = Scene.WRAP
		self.state = Character.runLeft


	def update(self):
		super().update()

      def walkBehavior(self):
        if self.scene.keysDown[K_RIGHT]:
          self.facing = Facing.RIGHT
          self.setCurrentCycle(Facing.RIGHT)
          self.startAnimation()
        elif self.scene.keysDown[K_LEFT] 
          self.facing = Facing.LEFT
          self.setCurrentCycle(Facing.LEFT)
          self.startAnimation()
          self.dx = -5
	def jumpBehavior(self):
		self.stateTimer = 60
		self.dy = -6			
          
        

	  # Add a method called walkBehavior. 
    # This should check if self.scene.keysDown[K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and 10
    # If not check if self.scene.keysDown[K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and -10
    
    # Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.

# 
# 42x30
# Lucas
# Sheet: 248 x 60
# Cell: 41 x 30
# super().__init__(thisScene, "yourimage.png", sheetX, sheetY)
# loadAnimation(sheetX, sheetY, CellX, cellY)
class Lucas(Character):
	def __init__(self,thisScene):
		super().__init__(thisScene,"sprites/lucas_sprite.png", 200,200)
		self.x = 100
		self.y = 100
				self.loadAnimation(496, 120, 82, 60)
		self.generateAnimationCycles()
		self.setAnimationSpeed(100)	


		self.dy= 1
		self.dx= 1
	    	def walkBehavior(self):
		if self.scene.keysDown[K_RIGHT]:
			self.facing = Facing.RIGHT
			self.setCurrentCycle(Facing.RIGHT)
			self.startAnimation()
		elif self.scene.keysDown[K_LEFT]:
			self.facing = Facing.LEFT
			self.setCurrentCycle(Facing.LEFT)
			self.startAnimation()
			def jumpBehavior(self):
				self.stateTimer = 50
				self.dy = -6
				def update(self):
			super().update()

		# Add a method called walkBehavior. 
    # This should check if self.scene.keysDown[K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and 10
    # If not check if self.scene.keysDown[K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and -10
    
    # Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.

# sheet 432x358
# cell Anthony 144x179
class Anthony(Character):
	def __init__(self, thisScene):
		super().__init__(thisScene, "sprites/anthony_sprite.png", 100, 100)
		self.x = 200
		self.y = 500
		self.dy = 1
		self.dx = 6

		# super().__init__(thisScene, "filename.png", sheetX, sheetY)
	super().__init__(thisScene, "filename.png", sheet432,sheet179)
			def walkBehavior(self):
		if , self.scene.keysDown[K_RIGHT]:
			self.facing = Facing.RIGHT
			self.setCurrentCycle(Facing.RIGHT)
			self.startAnimation()
			self.dx = 7
		elif self.scene.keysDown[K_LEFT]:
			self.facing = Facing.LEFT
			self.setCurrentCycle(Facing.LEFT)
			self.startAnimation(
			self.dx = -7
			self.stateTimer = 40
	def update(self):
		super().update()

	# Add a method called walkBehavior. 
  # This should check if self.scene.keysDown[K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and 10
  
  # If not check if self.scene.keysDown[K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and -10
    
  # Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.
		

# Make a class that inherits character
#Sophie's Character
# 75 x 50
# Sheet: 144x64
# cell: 48x32
class Sophie(Character):
  def __init__(self, thisScene):
    super().__init__(thisScene, "sprites/sophie_sprite.png", 144, 64)
    self.x += 75
    self.y += 50
    self.dx = 1
    self.dy = -1
    self.boundAction = Scene.WRAP

		# add loadAnimation, generateAnimation, setAnimationSpeed, and playAnimation methods
    self.loadAnimation(144, 64, 48, 32)
    self.generateAnimationCycles()
    self.SrtAnimationSpeed(100)
    self.playAnimation()
    self.dx = 1
    self.dy = -1
    self.boundAction = Scene.WRAP
    self.state = States.FALLING
			
	# Add a method called walkBehavior. 
  # This should check if self.scene.keysDown[K_RIGHT]is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and 10
  # If not check if self.scene.keysDown[K_LEFT] is True. If so self.facing to Facing.RIGHT, self.setCurrentCycle to Facing.RIGHT, call the self.startAnimation method. Set the DX to a value between 0 and -10
  def walkBehavior(self):
    if self.scene.keysDown[K-RIGHT]:
      self.facing = Facing.RIGHT
      self.setCurrentCycle(Facing.RIGHT)
      self.startAnimation()
      self.dx = 3
      elif self.scene.keysDown[K-LEFT]:
        self.facing = Facing.LEFT
        self.setCurrentCycle(Facing.LEFT)
        self.startAnimation()
        self.dx = -3
  
  # Add a method called jumpBehavior. This should set the dy to a negative number (moving up), and set the stateTimer to the number of frames before falling.
  def jumpBehavior(self):
    self.startTimer = 50
    self.dy = -6
    def update(self):
      super().update()



# Sean's Sprite Sheet
# 50x50 sheet
# https://opengameart.org/content/cat-fighter-sprite-sheet
# Cat by DogChicken @ OpenGameArt.org

# Lucas sprite sheet
# 41x30
# https://opengameart.org/content/esquire-animated-classic-hero-edit
# Knight by Umz @http://umzgames.com/
# villan: https://opengameart.org/content/monster-green
# by PiXeRaT @ OpenGameArt.org

# Siqi's sprite sheet - needs sprite sheet
# sheet 41x30
# https://opengameart.org/content/ninja-animated----hero
# https://opengameart.org/content/explosion-sheet

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

#Forest Pack
#ansimuz @ openGameArt.org
# https://opengameart.org/content/forest-background



class Game(Scene):
	def __init__(self):
		super().__init__(600,600)
		self.bg0 = Background(self, "sprites/parallax-forest-back-trees.png", 1020, 600, .25, 0)
		self.bg1 = Background(self, "sprites/parallax-forest-middle-trees.png", 1020, 600, .5, 0)		
		self.bg2 = Background(self, "sprites/parallax-forest-front-trees.png", 1020, 600, .75, 0)
		self.bg3 = Background(self, "sprites/parallax-forest-lights.png", 1020, 600, 1, 0)		
		self.ground = Ground(self)

		self.ian = Ian(self)

		self.johnny = Johnny(self)
		

	
    
	def updateGame(self):
		self.bg0.update()
		self.bg1.update()
		self.bg2.update()
		self.bg3.update()
		self.ground.update()

		# player sprites
		self.ian.update()
		self.johnny.update()
	

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