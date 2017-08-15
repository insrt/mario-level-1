# Author : Will Robinson

import pygame
import constants as c

class Textures(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.spritesheet = pygame.image.load('sprites/tile_set.png')
		self.load_images()
		self.tile_map()
		# self.image = self.textures[self.map[0][1]]
		# self.rect = self.image.get_rect()



	def load_images(self):
		self.textures = {
		'brick' : self.get_image(208,0,16,16),
		'ground_brick' : self.get_image(0,0,16,16),
		'mystery_box' : [self.get_image(384,0,16,16), # Mystery box sequence  [0]
						 self.get_image(400,0,16,16), # Mystery box sequence  [1]
						 self.get_image(416,0,16,16), # Mystery box sequence  [2]
						 self.get_image(432,0,16,16)], # Opened mystery box   [3]

		'coin' : [self.get_image(384,16,16,16), # Coin sequence  [0]
				  self.get_image(400,16,16,16), # Coin sequence  [1]
				  self.get_image(416,16,16,16)], # Coin sequence [2]

		'step_block' : self.get_image(0,16,16,16),

		'cloud' : [self.get_image(0,320,16,16), # Cloud left-half top       [0]
				   self.get_image(0,336,16,16), # Cloud left-half bottom    [1]
				   self.get_image(16,320,16,16), # Cloud middle top         [2]
				   self.get_image(16,336,16,16), # Cloud middle bottom      [3]
				   self.get_image(32,320,16,16), # Cloud right-half top     [4]
				   self.get_image(32,336,16,16)], # Cloud right-half bottom  [5]

		'green_pipe' : [self.get_image(0,128,16,16), # Upward facing pipe left-top       [0]
						self.get_image(0,144,16,16), # Upward facing pipe left-bottom    [1]
						self.get_image(16,128,16,16), # Upward facing pipe right-top     [2]
						self.get_image(16,144,16,16), # Upward facing pipe right-bottom  [3]
						self.get_image(32,128,16,16), # Left facing pipe left-top        [4]
						self.get_image(32,144,16,16), # Left facing pipe left-bottom     [5] 
						self.get_image(48,128,16,16), # Left facing pipe right-top       [6]
						self.get_image(48,144,16,16)], # Left facing pipe right-bottom   [7]

		'sky' : self.get_image(48,328,16,16),

		'bush' : [self.get_image(176,144,16,16), # bush left   [0]
				  self.get_image(192,144,16,16), # bush middle [1]
				  self.get_image(208,144,16,16)], # bush right [2]

		'hill' : [self.get_image(128,128,16,16), # left-side slant    [0]
				  self.get_image(128,144,16,16), # right corner dots  [1]
				  self.get_image(144,128,16,16), # top curve          [2]
				  self.get_image(144,144,16,16), # solid green        [3]
				  self.get_image(160,128,16,16), # right-side slant   [4]
				  self.get_image(160,144,16,16)], # left corner dots  [5]
		}

	def tile_map(self):
		self.map = [['brick','sky','step_block']]
		# print(self.textures['coin'][1])


	def get_image(self, x, y, width, height):
		#retrieves image from spritesheet
		image = pygame.Surface((width, height))
		image.fill(c.SKY_BLUE)
		image.blit(self.spritesheet, (0,0), (x,y,width,height)) #TODO - upscale images
		# pygame.mask.from_surface(image)
		return image

class Tile(pygame.sprite.Sprite):
	def __init__(self,game,texture,row,col,floor=False, obstacle=True):
		if floor:
			self.groups = game.all_sprites, game.tiles, game.floor
		elif not obstacle:
			self.groups = game.all_sprites, game.tiles
		else:
			self.groups = game.all_sprites, game.tiles, game.obstacles
		pygame.sprite.Sprite.__init__(self, self.groups) 

		self.game = game
		self.image = texture
		# self.image.set_colorkey(c.BLACK)
		self.rect = self.image.get_rect()
		self.x = row
		self.y = col
		self.rect.x = row*c.TILESIZE
		self.rect.y = col*c.TILESIZE

	def getX(self):
		return self.rect.x
		
	def getY(self):
		return self.rect.y
