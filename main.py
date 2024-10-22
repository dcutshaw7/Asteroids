import pygame
from constants import *
from circleshape import * 
from player import * 
from asteroid import * 
from asteroidfield import *


def main(): 
	pygame.init() 	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group() 
	clock = pygame.time.Clock()
	dt = 0 
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2 
	player = Player(x, y) 
	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable) 
	AsteroidField.containers = (updatable,)
	Asteroid_Field = AsteroidField() 
	updatable.add(player)
	drawable.add(player)
	while True: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit() 
				return 
		screen.fill((0,0,0)) 
		updatable.update(dt)
		for sprite in drawable: 
			sprite.draw(screen) 
		pygame.display.flip()
			
		dt = clock.tick(60) / 1000  
if __name__ == "__main__": 
	main() 


























if __name__ == "__main__":
	main()
