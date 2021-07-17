from Game.Sprite import Sprite
from Game.Block import Block

class Ground(Block):
	def __init__(self, thisScene):
		spriteMaker = [["sprites/ground.png"] ] *30
		super().__init__(thisScene, spriteMaker, 120, 40)
		self.x = 0
		self.y = 500
		
	def update(self, offsetX = 0, offsetY = 0):
				
		super().update(offsetX, offsetY)