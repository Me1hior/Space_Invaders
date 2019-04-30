# Kогда в нашу игру добавляется новая функциональность, также в нее
#    обычно добавляются новые настройки 
# Этот модуль содержит класс с именем Settings для хранения всех настроек. 
# Такое решение позволит передавать один объект вместо множества отдельных настроек. 
# Jно упрощает вызовы функций и упрощает изменение внешнего вида игры с ростом проекта. 
# Чтобы внести изменения в игру, достаточно будет изменить некоторые значения в settings.py 
#    вместо того, чтобы искать разные настройки в файлах.

class Settings():
	"""Класс для хранения всех настроек игры Alien Invasion."""
	
	def __init__(self):
		"""Инициализирует статические настройки игры."""
	
		# Параметры экрана
		self.screen_width = 1600
		self.screen_height = 800
		self.bg_color = (117, 187, 253)
		
		# Настройки корабля
		self.ship_limit = 3
		
		# Параметры пули
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 5

		# Настройки пришельцев
		self.fleet_drop_speed = 10

		# Темп ускорения игры
		self.speedup_scale = 1.1
		
		# Темп роста стоимости пришельцев
		self.score_scale = 1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Инициализирует настройки, изменяющиеся в ходе игры."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		self.fleet_direction = 1				# fleet_direction = 1 обозначает движение вправо; а -1 - влево
		
		# Подсчет очков
		self.alien_points = 50
		
	def increase_speed(self):
		"""Увеличивает настройки скорости и стоимость пришельцев."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		
