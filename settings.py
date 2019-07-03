class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """initialise the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230) # light grey

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_color = (60, 60, 60)
        self.bullet_height = 15
        self.bullet_width = 3
