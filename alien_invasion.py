import sys
import pygame

class AlienInvasion:
	"""Overall class to manage game assets and behaviours."""

	def __init__(self):
		"""Initialise the game, and create game resources."""
		pygame.init()
		self.screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			# Watch for keyboarad and mouse events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# Make the most recently drawn screen visible
			pygame.display.filp()

if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()