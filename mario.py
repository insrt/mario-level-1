# Author : Will Robinson

import pygame 
import constants as c

vec = pygame.math.Vector2


class Mario(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		self.walking = False
		self.jumping = False
		self.colliding = False
		self.current_frame = 0
		self.last_update = 0
		self.spritesheet = pygame.image.load('sprites/mario_bros.png')
		self.load_images()
		self.image = self.right_normal_small_mario[0]
		# self.image = pygame.Surface((30, 40))
		# self.image.fill(c.RED)
		self.rect = self.image.get_rect()
		self.obstacle = False
		self.pos = vec(c.WIDTH/4, c.HEIGHT/4)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)
		self.jump_power = -3.0
		self.jump_cut_mag = -2.0
		self.FACING_LEFT = False
		self.BIG_MARIO = False
		self.FIRE_POWER = False
		self.STAR_POWER = False
	
	def collide(self):
		pass

	def update(self):
		self.animate()
		self.acc = vec(0,0.4)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.acc.x = -c.MARIO_ACC
		if keys[pygame.K_RIGHT]:
			self.acc.x = c.MARIO_ACC
		if keys[pygame.K_z]:
			self.vel.y = self.jump_power
		

  

		#friction
		self.acc.x += self.vel.x * c.MARIO_FRICTION
		#equations of motion
		self.vel += self.acc
		if abs(self.vel.x) < c.MARIO_ACC:
			self.vel.x = 0

				

		self.pos += self.vel + 0.5 * self.acc	

		self.rect.midbottom = self.pos
		self.colliding = False
		for tile in self.game.obstacles:
			
			if self.rect.colliderect(tile):
				self.colliding = True
				if not self.FACING_LEFT and self.walking:
					self.pos.x = tile.rect.left-8
					self.vel.x = 0
				elif self.FACING_LEFT and self.walking:
					self.pos.x = tile.rect.right+8
					self.vel.x = 0
				elif self.jumping and self.pos.y < tile.rect.y-1:
					self.jumping = False
					self.pos.y = tile.rect.top
					self.vel.y = 0
		self.rect.midbottom = self.pos


	def collide(self):
		for t in self.game.obstacles:
			if pygame.sprite.collide_rect(self, t):
				if self.vel.x > 0: 
					self.rect.right = t.rect.left
					print('collide right')
				if self.vel.x < 0:
					self.rect.left = t.rect.right
					print('collide left')
				if self.vel.y > 0:
					self.rect.bottom = t.rect.top
					# self.vel.y = 0
				if self.vel.y <= 0:
					self.rect.top = t.rect.bottom

	def load_images(self):
		self.right_facing = []
		self.left_facing  = []

		#right facing sprites
		self.right_normal_small_mario = []
		self.right_fire_small_mario = []
		self.right_star_small_black_mario = []
		self.right_star_small_green_mario = []
		self.right_star_small_red_mario = []

		self.right_normal_big_mario = []
		self.right_fire_big_mario = []
		self.right_star_big_black_mario = []
		self.right_star_big_green_mario = []
		self.right_star_big_red_mario = []

		#normal small mario
		self.right_normal_small_mario.append(
			self.get_image(176,32,16,16)) #right standing [0]
		self.right_normal_small_mario.append(
			self.get_image(80,32,16,16)) #right walking 1 [1]
		self.right_normal_small_mario.append(
			self.get_image(96,32,16,16)) #right walking 2 [2]
		self.right_normal_small_mario.append(
			self.get_image(112,32,16,16)) #right walking 3 [3]
		self.right_normal_small_mario.append(
			self.get_image(128,32,16,16)) #right slide [4]
		self.right_normal_small_mario.append(
			self.get_image(144,32,16,16)) #right jump [5]
		self.right_normal_small_mario.append(
			self.get_image(160,32,16,16)) #death [6]
		self.right_normal_small_mario.append(
			self.get_image(192,32,16,16)) #right flag 1 [7]
		self.right_normal_small_mario.append(
			self.get_image(208,32,16,16)) #right flag 2 [8]
		
		#fire small mario
		self.right_fire_small_mario.append(
			self.get_image(176,80,16,16)) #right standing [0]
		self.right_fire_small_mario.append(
			self.get_image(80,80,16,16)) #right walking 1 [1]
		self.right_fire_small_mario.append(
			self.get_image(96,80,16,16)) #right walking 2 [2]
		self.right_fire_small_mario.append(
			self.get_image(112,80,16,16)) #right walking 3 [3]
		self.right_fire_small_mario.append(
			self.get_image(128,80,16,16)) #right slide [4]
		self.right_fire_small_mario.append(
			self.get_image(144,80,16,16)) #right jump [5]
		self.right_fire_small_mario.append(
			self.get_image(160,80,16,16)) #death [6]
		self.right_fire_small_mario.append(
			self.get_image(192,80,16,16)) #right flag 1 [7]
		self.right_fire_small_mario.append(
			self.get_image(208,80,16,16)) #right flag 2 [8]

		#black small mario  (star mario sequence)
		self.right_star_small_black_mario.append(
			self.get_image(176,176,16,16)) #right standing [0]
		self.right_star_small_black_mario.append(
			self.get_image(80,176,16,16)) #right walking 1 [1]
		self.right_star_small_black_mario.append(
			self.get_image(96,176,16,16)) #right walking 2 [2]
		self.right_star_small_black_mario.append(
			self.get_image(112,176,16,16)) #right walking 3 [3]
		self.right_star_small_black_mario.append(
			self.get_image(128,176,16,16)) #right slide [4]
		self.right_star_small_black_mario.append(
			self.get_image(144,176,16,16)) #right jump [5]


		
		#green small mario (star mario sequence)
		self.right_star_small_green_mario.append(
			self.get_image(176,208,16,16)) #right standing [0]
		self.right_star_small_green_mario.append(
			self.get_image(80,208,16,16)) #right walking 1 [1]
		self.right_star_small_green_mario.append(
			self.get_image(96,208,16,16)) #right walking 2 [2]
		self.right_star_small_green_mario.append(
			self.get_image(112,208,16,16)) #right walking 3 [3]
		self.right_star_small_green_mario.append(
			self.get_image(128,208,16,16)) #right slide [4]
		self.right_star_small_green_mario.append(
			self.get_image(144,208,16,16)) #right jump [5]


		#red small mario (star mario sequence)
		self.right_star_small_red_mario.append(
			self.get_image(176,256,16,16)) #right standing [0]
		self.right_star_small_red_mario.append(
			self.get_image(80,256,16,16)) #right walking 1 [1]
		self.right_star_small_red_mario.append(
			self.get_image(96,256,16,16)) #right walking 2 [2]
		self.right_star_small_red_mario.append(
			self.get_image(112,256,16,16)) #right walking 3 [3]
		self.right_star_small_red_mario.append(
			self.get_image(128,256,16,16)) #right slide [4]
		self.right_star_small_red_mario.append(
			self.get_image(144,256,16,16)) #right jump [5]



		#normal big mario
		self.right_normal_big_mario.append(
			self.get_image(176,0,16,32)) #right standing [0]
		self.right_normal_big_mario.append(
			self.get_image(80,0,16,32)) #right walking 1 [1]
		self.right_normal_big_mario.append(
			self.get_image(96,0,16,32)) #right walking 2 [2]
		self.right_normal_big_mario.append(
			self.get_image(112,0,16,32)) #right walking 3 [3]
		self.right_normal_big_mario.append(
			self.get_image(128,0,16,32)) #right slide [4]
		self.right_normal_big_mario.append(
			self.get_image(144,0,16,32)) #right jump [5]
		self.right_normal_big_mario.append(
			self.get_image(160,0,16,32)) #crouch [6]
		self.right_normal_big_mario.append(
			self.get_image(192,0,16,32)) #right flag 1 [7]
		self.right_normal_big_mario.append(
			self.get_image(208,0,16,32)) #right flag 2 [8]
		self.right_normal_big_mario.append(
			self.get_image(320,0,16,32)) #big to small transition [9]


		#fire big mario
		self.right_fire_big_mario.append(
			self.get_image(176,48,16,32)) #right standing [0]
		self.right_fire_big_mario.append(
			self.get_image(80,48,16,32)) #right walking 1 [1]
		self.right_fire_big_mario.append(
			self.get_image(96,48,16,32)) #right walking 2 [2]
		self.right_fire_big_mario.append(
			self.get_image(112,48,16,32)) #right walking 3 [3]
		self.right_fire_big_mario.append(
			self.get_image(128,48,16,32)) #right slide [4]
		self.right_fire_big_mario.append(
			self.get_image(144,48,16,32)) #right jump [5]
		self.right_fire_big_mario.append(
			self.get_image(160,48,16,32)) #crouch [6]
		self.right_fire_big_mario.append(
			self.get_image(192,48,16,32)) #right flag 1 [7]
		self.right_fire_big_mario.append(
			self.get_image(208,48,16,32)) #right flag 2 [8]

		#black big mario (star mario sequence)
		self.right_star_big_black_mario.append(
			self.get_image(176,96,16,32)) #right standing [0]
		self.right_star_big_black_mario.append(
			self.get_image(80,96,16,32)) #right walking 1 [1]
		self.right_star_big_black_mario.append(
			self.get_image(96,96,16,32)) #right walking 2 [2]
		self.right_star_big_black_mario.append(
			self.get_image(112,96,16,32)) #right walking 3 [3]
		self.right_star_big_black_mario.append(
			self.get_image(128,96,16,32)) #right slide [4]
		self.right_star_big_black_mario.append(
			self.get_image(144,96,16,32)) #right jump [5]
		self.right_star_big_black_mario.append(
			self.get_image(160,96,16,32)) #crouch [6]

		#green big mario (star mario sequence)
		self.right_star_big_green_mario.append(
			self.get_image(176,144,16,32)) #right standing [0]
		self.right_star_big_green_mario.append(
			self.get_image(80,144,16,32)) #right walking 1 [1]
		self.right_star_big_green_mario.append(
			self.get_image(96,144,16,32)) #right walking 2 [2]
		self.right_star_big_green_mario.append(
			self.get_image(112,144,16,32)) #right walking 3 [3]
		self.right_star_big_green_mario.append(
			self.get_image(128,144,16,32)) #right slide [4]
		self.right_star_big_green_mario.append(
			self.get_image(144,144,16,32)) #right jump [5]
		self.right_star_big_green_mario.append(
			self.get_image(160,144,16,32)) #crouch [6]


		#red big mario (star mario sequence)
		self.right_star_big_red_mario.append(
			self.get_image(176,192,16,32)) #right standing [0]
		self.right_star_big_red_mario.append(
			self.get_image(80,192,16,32)) #right walking 1 [1]
		self.right_star_big_red_mario.append(
			self.get_image(96,192,16,32)) #right walking 2 [2]
		self.right_star_big_red_mario.append(
			self.get_image(112,192,16,32)) #right walking 3 [3]
		self.right_star_big_red_mario.append(
			self.get_image(128,192,16,32)) #right slide [4]
		self.right_star_big_red_mario.append(
			self.get_image(144,192,16,32)) #right jump [5]
		self.right_star_big_red_mario.append(
			self.get_image(160,192,16,32)) #crouch [6]

		#left facing sprites
		self.left_normal_small_mario = []
		self.left_fire_small_mario = []
		self.left_star_small_black_mario = []
		self.left_star_small_green_mario = []
		self.left_star_small_red_mario = []

		self.left_normal_big_mario = []
		self.left_fire_big_mario = []
		self.left_star_big_black_mario = []
		self.left_star_big_green_mario = []
		self.left_star_big_red_mario = []

		for frame in self.right_normal_small_mario:
			frame.set_colorkey(c.BLACK)
			self.left_normal_small_mario.append(pygame.transform.flip(frame,True,False))

		for frame in self.right_fire_small_mario:
			frame.set_colorkey(c.BLACK)
			self.left_fire_small_mario.append(pygame.transform.flip(frame,True,False))

		for frame in self.right_star_small_black_mario:
			frame.set_colorkey(c.BLACK)
			self.left_star_small_black_mario.append(pygame.transform.flip(frame,True,False))

		for frame in self.right_star_small_green_mario:
			frame.set_colorkey(c.BLACK)
			self.left_star_small_green_mario.append(pygame.transform.flip(frame,True,False))

		for frame in self.right_star_small_red_mario:
			frame.set_colorkey(c.BLACK)
			self.left_star_small_red_mario.append(pygame.transform.flip(frame,True,False))


		for frame in self.right_normal_big_mario:
			frame.set_colorkey(c.BLACK)
			self.left_normal_big_mario.append(pygame.transform.flip(frame,True,False))

		for frame in self.right_fire_big_mario:
			frame.set_colorkey(c.BLACK)
			self.left_fire_big_mario.append(pygame.transform.flip(frame,True,False))

		for frame in self.right_star_big_black_mario:
			frame.set_colorkey(c.BLACK)
			self.left_star_big_black_mario.append(pygame.transform.flip(frame,True,False))

		for frame in self.right_star_big_green_mario:
			frame.set_colorkey(c.BLACK)
			self.left_star_big_green_mario.append(pygame.transform.flip(frame,True,False))

		for frame in self.right_star_big_red_mario:
			frame.set_colorkey(c.BLACK)
			self.left_star_big_red_mario.append(pygame.transform.flip(frame,True,False))

	def get_image(self, x, y, width, height):
		#retrieves image from spritesheet
		image = pygame.Surface((width, height))
		image.blit(self.spritesheet, (0,0), (x,y,width,height)) #TODO - upscale images
		# pygame.mask.from_surface(image)
		return image

	def jump(self):
		pass

	def animate(self):
		current_time = pygame.time.get_ticks()

		if self.vel.x != 0:
			self.walking = True
		else:
			self.walking = False

		if self.vel.y != 0:
			self.jumping = True
		else:
			self.jumping = False
		if self.walking:
			if current_time > 500:
				self.last_update = current_time
				self.current_frame = (self.current_frame + 1) % 4
				if self.vel.x > 0:
					self.FACING_LEFT = False
					if not self.BIG_MARIO and not self.FIRE_POWER and not self.STAR_POWER:
						self.image = self.right_normal_small_mario[self.current_frame]
						self.rect = self.image.get_rect()
					elif self.FIRE_POWER and not self.BIG_MARIO and not self.STAR_POWER:
						self.image = self.right_fire_small_mario[self.current_frame]
						self.rect = self.image.get_rect()
					#implement star power sprites right here

					elif self.BIG_MARIO and not self.FIRE_POWER and not self.STAR_POWER:
						self.image = self.right_normal_big_mario[self.current_frame]
						self.rect = self.image.get_rect()
					elif self.BIG_MARIO and self.FIRE_POWER and not self.STAR_POWER:
						self.image = self.right_fire_big_mario[self.current_frame]
						self.rect = self.image.get_rect()
					#implement star power sprites right here

				else:
					self.FACING_LEFT = True
					if not self.BIG_MARIO and not self.FIRE_POWER and not self.STAR_POWER:
						self.image = self.left_normal_small_mario[self.current_frame]
						self.rect = self.image.get_rect()
					elif self.FIRE_POWER and not self.BIG_MARIO and not self.STAR_POWER:
						self.image = self.left_fire_small_mario[self.current_frame]
						self.rect = self.image.get_rect()
					#implement star power sprites right here

					elif self.BIG_MARIO and not self.FIRE_POWER and not self.STAR_POWER:
						self.image = self.left_normal_big_mario[self.current_frame]
						self.rect = self.image.get_rect()
					elif self.BIG_MARIO and self.FIRE_POWER and not self.STAR_POWER:
						self.image = self.left_fire_big_mario[self.current_frame]
						self.rect = self.image.get_rect()
				#implement star power sprites right here


		if self.jumping:
			if not self.FACING_LEFT:
				if not self.BIG_MARIO and not self.FIRE_POWER and not self.STAR_POWER:
					self.image = self.right_normal_small_mario[5]
					self.rect = self.image.get_rect()

				elif self.FIRE_POWER and not self.BIG_MARIO and not self.STAR_POWER:
					self.image = self.right_fire_small_mario[5]
					self.rect = self.image.get_rect()

				elif self.BIG_MARIO and not self.FIRE_POWER and not self.STAR_POWER:
					self.image = self.right_normal_big_mario[5]

				elif self.BIG_MARIO and self.FIRE_POWER and not self.STAR_POWER:
					self.image = self.right_fire_big_mario[5]

			else:
				if not self.BIG_MARIO and not self.FIRE_POWER and not self.STAR_POWER:
					self.image = self.left_normal_small_mario[5]
					self.rect = self.image.get_rect()

				elif self.FIRE_POWER and not self.BIG_MARIO and not self.STAR_POWER:
					self.image = self.left_fire_small_mario[5]
					self.rect = self.image.get_rect()

				elif self.BIG_MARIO and not self.FIRE_POWER and not self.STAR_POWER:
					self.image = self.left_normal_big_mario[5]

				elif self.BIG_MARIO and self.FIRE_POWER and not self.STAR_POWER:
					self.image = self.left_fire_big_mario[5]

		if not self.walking and not self.jumping:
			self.current_frame = 0
			if not self.FACING_LEFT:
				if not self.BIG_MARIO and not self.FIRE_POWER and not self.STAR_POWER:
					self.image = self.right_normal_small_mario[self.current_frame]
					self.rect = self.image.get_rect()
				elif not self.BIG_MARIO and self.FIRE_POWER and not self.STAR_POWER:
					self.image = self.right_fire_small_mario[self.current_frame]
					self.rect = self.image.get_rect()
				#implement star power sprites right here

				elif self.BIG_MARIO and not self.FIRE_POWER and not self.STAR_POWER:
					self.image = self.right_normal_big_mario[self.current_frame]
					self.rect = self.image.get_rect()
				elif self.BIG_MARIO and self.FIRE_POWER and not self.STAR_POWER:
					self.image = self.right_fire_big_mario[self.current_frame]
					self.rect = self.image.get_rect()
				#implement star power sprites right here

			else:
				if not self.BIG_MARIO and not self.FIRE_POWER and not self.STAR_POWER:
					self.image = self.left_normal_small_mario[self.current_frame]
					self.rect = self.image.get_rect()
				elif not self.BIG_MARIO and self.FIRE_POWER and not self.STAR_POWER:
					self.image = self.left_fire_small_mario[self.current_frame]
					self.rect = self.image.get_rect()
				#implement star power sprites right here

				elif self.BIG_MARIO and not self.FIRE_POWER and not self.STAR_POWER:
					self.image = self.left_normal_big_mario[self.current_frame]
					self.rect = self.image.get_rect()
				elif self.BIG_MARIO and self.FIRE_POWER and not self.STAR_POWER:
					self.image = self.left_fire_big_mario[self.current_frame]
					self.rect = self.image.get_rect()
				#implement star power sprites right here

