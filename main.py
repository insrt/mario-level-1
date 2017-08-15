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
		self.floor = pygame.sprite.Group() #group for floor tiles -- necessary for collision testing
		self.obstacles = pygame.sprite.Group()
		self.mario = Mario(g)
		
		self.level_one = Textures()
		for row, tiles in enumerate(self.level_one_data):
			for col, tile in enumerate(tiles):
				if tile == 'q':
					Tile(self, self.level_one.textures['mystery_box'][0], col, row)

				if tile == 'r':
					Tile(self, self.level_one.textures['brick'], col, row)

				if tile == 'a':
					Tile(self, self.level_one.textures['ground_brick'], col, row, True)
				
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
					if self.level_one_data[row][col-1] != 'c' and self.level_one_data[row+1][col] == 'c':
						Tile(self, self.level_one.textures['cloud'][0], col, row, False, False)
					elif self.level_one_data[row][col-1] != 'c' and self.level_one_data[row+1][col] != 'c':
						Tile(self, self.level_one.textures['cloud'][1], col, row, False, False)
					elif self.level_one_data[row-1][col] != 'c' and self.level_one_data[row][col-1] == 'c' and self.level_one_data[row][col+1] == 'c':
						Tile(self, self.level_one.textures['cloud'][2], col, row, False, False)
					elif self.level_one_data[row-1][col] == 'c' and self.level_one_data[row][col-1] == 'c' and self.level_one_data[row][col+1] == 'c':
						Tile(self, self.level_one.textures['cloud'][3], col, row, False, False)
					elif self.level_one_data[row+1][col] == 'c' and self.level_one_data[row][col+1] != 'c':
						Tile(self, self.level_one.textures['cloud'][4], col, row, False, False)
					elif self.level_one_data[row][col+1] != 'c' and self.level_one_data[row+1][col] != 'c':
						Tile(self, self.level_one.textures['cloud'][5], col, row, False, False)

				if tile == 's':
					Tile(self, self.level_one.textures['step_block'], col, row)

				if tile == 'b':
					if self.level_one_data[row][col-1] != 'b':
						Tile(self, self.level_one.textures['bush'][0], col, row, False, False)
					elif self.level_one_data[row][col+1] == 'b':
						Tile(self, self.level_one.textures['bush'][1], col, row, False, False)
					else:
						Tile(self, self.level_one.textures['bush'][2], col, row, False, False)
				if tile == 'h':
					if self.level_one_data[row][col-1] != 'h' and self.level_one_data[row-1][col] != 'h' and self.level_one_data[row][col+1] == 'h':
						Tile(self, self.level_one.textures['hill'][0], col, row, False, False)
					elif self.level_one_data[row][col+2] == 'h' and self.level_one_data[row][col+2] == 'h':
						Tile(self, self.level_one.textures['hill'][3], col, row, False, False)
					elif self.level_one_data[row][col+1] == 'h' and self.level_one_data[row][col-2] != 'h' and self.level_one_data[row][col-1] == 'h':
						Tile(self, self.level_one.textures['hill'][1], col, row, False, False)
					elif self.level_one_data[row][col+2] != 'h' and self.level_one_data[row][col-1] == 'h' and self.level_one_data[row][col+1] == 'h': #fix right corner dots
						Tile(self, self.level_one.textures['hill'][5], col, row, False, False)
					elif self.level_one_data[row][col+1] != 'h' and self.level_one_data[row-1][col] != 'h' and self.level_one_data[row][col-1] == 'h':
						Tile(self, self.level_one.textures['hill'][4], col, row, False, False)
					else: 
						Tile(self, self.level_one.textures['hill'][2], col, row, False, False)
		self.all_sprites.add(self.mario)
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

		#scroll window if mario* reaches 3/4 mark on screen
		if not self.mario.colliding:
			if self.mario.rect.right >= c.WIDTH/2.75 and not self.mario.FACING_LEFT:
				 self.mario.pos.x += -self.mario.vel.x
				 for tile in self.tiles:
				 	tile.rect.x += -(abs(self.mario.vel.x))
		# elif self.mario.rect.x < c.WIDTH:
		# 	for tile in self.tiles:
		# 		tile.rect.x += 0

		#collisions
		floor_collide = pygame.sprite.spritecollide(self.mario, self.floor, False)
		if floor_collide:
			self.mario.pos.y = floor_collide[0].rect.top + 1
			self.mario.vel.y = 0
			self.mario.pos.x += self.mario.vel.x + 0.5 * self.mario.acc.x
		
		# collide = pygame.sprite.spritecollideany(self.mario, self.obstacles,collided=None)
		# print(collide)

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