import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to present a single alien in the fleet."""

	def __init__(self, ai_game):
		"""Initialise the alien and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load alien image and set its rect attribute."""
		self.image = pygame.image.load('images/alien.png')
		self.image = pygame.transform.scale(self.image, (self.settings.alien_width, self.settings.alien_height))
		self.rect = self.image.get_rect()

		# Start each alien near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's exact horizontal position.
		self.x = float(self.rect.x)
