import pygame 
import constants as c
from mario import *

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
		self.display.fill(c.BLACK)
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