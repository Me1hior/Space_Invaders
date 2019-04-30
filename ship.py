import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self, ai_settings, screen):		 		
		"""Инициализирует корабль и задает его начальную позицию."""
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		# Загрузка изображения корабля и получение прямоугольника.
		self.image = pygame.image.load('images/ufo.png')		# Загрузка изображения выполняется вызовом image.load()
																# Функция возвращает поверхность, представляющую корабль; 
																# полученный объект сохраняется в self.image.
																
		self.rect = self.image.get_rect()						# метод get_rect() используется для получения атрибута rect поверхности 
																# При работе с объектом rect для вас доступны координаты x и y верхней, нижней,
																# левой и правой сторон, а также центра. Присваивая любые из этих значений, вы
																# задаете текущую позицию прямоугольника.
												
		self.screen_rect = screen.get_rect()					# Корабль будет расположен в середине нижней стороны экрана. 
																# Для этого мы сначала сохраняем прямоугольник экрана в self.screen_rect

		# Каждый новый корабль появляется у нижнего края экрана.
		'''Местонахождение центра игрового элемента определяется атрибутами center,
		centerx или centery прямоугольника. '''				
		self.rect.centerx = self.screen_rect.centerx			# присваиваем self.rect.centerx (координата x центра корабля) 
																# значение атрибута centerx прямоугольника экрана 
		'''Стороны определяются атрибутами top,
		bottom, left и right.'''												
		self.rect.bottom = self.screen_rect.bottom				# Атрибуту self.rect.bottom (координата y низа корабля)
																# присваивается значение атрибута bottom прямоугольника экрана.
		# Сохранение вещественной координаты центра корабля.
		self.center = float(self.rect.centerx)
	 	
		# Флаг перемещения
		self.moving_right = False
		self.moving_left = False
		
		
	def update(self):
		"""Обновляет позицию корабля с учетом флага."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		self.rect.centerx = self.center
			
	def blitme(self):
		"""Рисует корабль в текущей позиции."""
		self.screen.blit(self.image, self.rect)					# метод blitme(), который выводит изображение на экран в позиции, заданной self.rect

	def center_ship(self):
		"""Размещает корабль в центре нижней стороны."""
		self.center = self.screen_rect.centerx
