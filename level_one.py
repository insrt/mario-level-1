# Author : Will Robinson

import pygame
import constants as c

class World(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.spritesheet = pygame.image.load('sprites/tile_set.png')
		self.load_images()
		self.tile_map()
		


	def load_images(self):
		self.textures = {
		'brick' : self.get_image(208,0,16,16),
		'ground_brick' : self.get_image(0,0,16,16),
		'mystery_box' : [self.get_image(384,0,16,16), # Mystery box sequence     [0]
						 self.get_image(400,0,16,16), # Mystery box sequence  [1]
						 self.get_image(416,0,16,16), # Mystery box sequence  [2]
						 self.get_image(432,0,16,16)], # Opened mystery box   [3]

		'coin' : [self.get_image(384,16,16,16), # Coin sequence    [0]
				  self.get_image(400,16,16,16), # Coin sequence  [1]
				  self.get_image(416,16,16,16)], # Coin sequence [2]

		'step_block' : self.get_image(0,16,16,16),

		'cloud' : [self.get_image(8,320,16,16), # Cloud left-half top [0]
				   self.get_image(8,336,16,16), # Cloud left-half bottom [1]
				   self.get_image(24,320,16,16),
				   self.get_image(24,336,16,16)], # Cloud right-half [2]

		'green_pipe' : [self.get_image(0,128,16,16), # Upward facing pipe left-top       [0]
						self.get_image(0,144,16,16), # Upward facing pipe left-bottom    [1]
						self.get_image(16,128,16,16), # Upward facing pipe right-top     [2]
						self.get_image(16,144,16,16), # Upward facing pipe right-bottom  [3]
						self.get_image(32,128,16,16), # Left facing pipe left-top        [4]
						self.get_image(32,144,16,16), # Left facing pipe left-bottom     [5] 
						self.get_image(48,128,16,16), # Left facing pipe right-top       [6]
						self.get_image(48,144,16,16)], # Left facing pipe right-bottom   [7]

		'sky' : self.get_image(48,328,16,16)
		}

	def tile_map(self):
		self.map = [['sky','brick']]


	def get_image(self, x, y, width, height):
		#retrieves image from spritesheet
		image = pygame.Surface((width, height))
		image.blit(self.spritesheet, (0,0), (x,y,width,height)) #TODO - upscale images

		return image


