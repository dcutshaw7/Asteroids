import pygame 
from circleshape import * 
from constants import * 
from main import * 
class Asteroid(CircleShape): 
	def __init__ (self, x , y , radius): 
		super().__init__(x, y , radius)
		self.velocity = pygame.Vector2(0,0) 
		self.x = x 
		self.y = y 
		self.radius = radius 


	def draw(self, screen): 
		pygame.draw.circle(screen, "white",(self. x, self. y), self. radius, 2)
	def update(self, dt): 
		self.x += self.velocity.x * dt 
		self.y += self.velocity.y * dt  