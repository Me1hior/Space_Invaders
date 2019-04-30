import sys
import pygame

class Ship():
	def __init__(self, screen):
		self.screen = screen
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		print(self.rect)
		
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
	def blitme(self):

		self.screen.blit(self.image, self.rect)

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	print(help(pygame))
	pygame.display.set_caption("Alien Invasion")
	bg_color = (230, 230, 230)
	ship = Ship(screen)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(bg_color)	
		ship.blitme()	
		pygame.display.flip()
run_game()
