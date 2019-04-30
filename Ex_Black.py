import pygame
import sys

def test():
	'''выводите значение атрибута event key'''
	
	pygame.init()
	screen = pygame.display.set_mode((600, 600))			
	pygame.display.set_caption("Тестирование экрана")
	
	while True:
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				sys.exit()
	
test()
