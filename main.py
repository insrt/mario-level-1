# Author : Will Robinson

import pygame
from os import path 
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
		self.load_data()

	def load_data(self):
		# load lives and other necessary data
		game_folder = path.dirname(__file__)
		self.level_one_data = []
		with open(path.join(game_folder, 'level_one_map.txt'), 'rt') as f:
			for line in f:
				self.level_one_data.append(line)

	def new(self):
		# start a new game
		self.all_sprites = pygame.sprite.Group()
		self.tiles = pygame.sprite.Group() #group for all texture tiles
		self.mario = Mario()
		self.all_sprites.add(self.mario)
		self.level_one = Textures()
		for row, tiles in enumerate(self.level_one_data):
			for col, tile in enumerate(tiles):
				if tile == 'q':
					Tile(self, self.level_one.textures['mystery_box'][0], col, row)

				if tile == 'r':
					Tile(self, self.level_one.textures['brick'], col, row)

				if tile == 'a':
					Tile(self, self.level_one.textures['ground_brick'], col, row)
				# if tile == '.':
				# 	Tile(self, self.level_one.textures['sky'], col, row)
				if tile == 'p':
					if self.level_one_data[row-1][col] != 'p' and tiles[col+1] == 'p':
						Tile(self, self.level_one.textures['green_pipe'][0], col, row) #right top

					elif tiles[col+1] == 'p':
						Tile(self, self.level_one.textures['green_pipe'][1], col, row) #right bottom

					elif self.level_one_data[row-1][col] !='p' and tiles[col+1]!='p':
						Tile(self,self.level_one.textures['green_pipe'][2], col, row) #left top

					else:
						Tile(self, self.level_one.textures['green_pipe'][3], col, row) #left bottom

				if tile == 'c':
					Tile(self, self.level_one.textures['cloud'][0], col, row)

				if tile == 's':
					Tile(self, self.level_one.textures['step_block'], col, row)
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
		# self.tiles.update()

		#scroll window if mario reaches 3/4 mark on screen
		if self.mario.rect.right >= c.WIDTH/2.75:
			 self.mario.pos.x += -self.mario.vel.x
			 for tile in self.tiles:
			 	tile.rect.x += -self.mario.vel.x
		elif self.mario.rect.left < c.WIDTH:
			for tile in self.tiles:
				tile.rect.x += 0


	def events(self):
		#game loop events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				if self.playing:
					self.playing = False
				self.running = False

	def draw(self):
		self.display.fill(c.SKY_BLUE)
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