import pygame
from constants import *
from circleshape import * 
from player import * 
from asteroid import * 
from asteroidfield import *
from shoot import *
import random 
import sys
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
	Shot.containers = (updatable, drawable)
	Asteroid_Field = AsteroidField() 
	updatable.add(player)
	drawable.add(player)
	while True: 
		dt = clock.tick(60) / 1000  
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit() 
				sys.exit()
		updatable.update(dt) 
		for asteroid in asteroids:
			if player.is_colliding_with(asteroid):
				print("Game over!")
				pygame.quit()
				sys.exit()

			for shot in updatable:
				if isinstance(shot, Shot): 
					if asteroid.is_colliding_with(shot):
						asteroid.kill()
						shot.kill()
		screen.fill((0,0,0)) 
		for sprite in drawable: 
			sprite.draw(screen) 
		pygame.display.flip()
 
if __name__ == "__main__": 
	main() 


























if __name__ == "__main__":
	main()
