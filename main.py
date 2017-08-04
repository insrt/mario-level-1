# Author : Will Robinson


import pygame 
import constants as c
from mario import *
from level_one import *

def game_exit():
	pygame.quit()
	quit()

class Game:
	def __init__(self):
		#initialize
		pygame.init()
		self.display = pygame.display.set_mode((c.WIDTH,c.HEIGHT))
		pygame.display.set_caption(c.TITLE)
		self.clock = pygame.time.Clock()
		self.running = True

	def load_data(self):
		# load lives and other necessary data
		pass

	def new(self):
		# start a new game
		self.all_sprites = pygame.sprite.Group()
		self.mario = Mario()
		self.all_sprites.add(self.mario)
		self.level_one = World()
		for row in range(len(self.level_one.map)):
			for column in range(len(self.level_one.map[row])):
				self.level_one.image = self.level_one.textures[self.level_one.map[row][column]]
				self.level_one.rect = self.level_one.image.get_rect()
				self.all_sprites.add(self.level_one)
		print(self.all_sprites)
		self.run()

	def run(self):
		# game loop
		self.playing = True
		while self.playing:
			self.clock.tick(c.FPS)
			self.events()
			self.update()
			self.draw()

	def update(self):
		self.all_sprites.update()

	def events(self):
		#game loop events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				if self.playing:
					self.playing = False
				self.running = False

	def draw(self):
		self.display.fill(c.SKY_BLUE)
		# for row in range(c.HEIGHT):
		# 	for column in range(c.WIDTH):
		# 		# print(self.level_one.textures[self.level_one.map[0][0]])
		# 		pygame.draw.rect(self.display, self.level_one.textures[self.level_one.map[row][column]], (column*c.TILE_WIDTH,row*c.TILE_HEIGHT,c.TILE_WIDTH,c.TILE_HEIGHT))
		self.all_sprites.draw(self.display)
		pygame.display.update()

	def start_screen(self):
		# start screen
		pass

	def game_over(self):
		#game over screen
		pass

g = Game()
g.start_screen()

while g.running:
	g.new()
	g.game_over()

game_exit()