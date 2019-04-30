import sys												
import pygame											# Cодержит функциональность, необходимую для создания игры
from settings import Settings							# Загружаем настройки
from ship import Ship									# Загружаем класс корабля
import game_functions as gf								# Загружаем функциональность
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

def run_game():											
	'''Инициализируем игру'''
	pygame.init()										# Инициализирует настройки, необходимые Pygame для работы
	ai_settings = Settings()							# создает экземпляр Settings и сохраняет его в ai_settings
	
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))			#создаем игровое окно
	pygame.display.set_caption("Alien Invasion")
	
	# Создание кнопки Play.
	play_button = Button(ai_settings, screen, "Play")

	# Создание экземпляров GameStats и Scoreboard.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	ship = Ship(ai_settings, screen)					# Создание корабля.
	bullets = Group()									# Создание группы для хранения пуль.
	aliens = Group()
	
	# Создание флота пришельцев.
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	
	while True:											# Запуск основного цикла игры.						
		
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)		# цикл проверяет ввод, полученный от игрока
		if stats.game_active:
			ship.update()									#  обновляет позицию корабля
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)						#  обновляет позицию всех выпущенных пуль
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)	# обновленные позиции игровых элементов используются для вывода нового экрана											
run_game()

