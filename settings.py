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
        self.ship_width = 50
        self.ship_height = 60

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_color = (60, 60, 60)
        self.bullet_height = 15
        self.bullet_width = 3

        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 0.8
        self.alien_width = 80
        self.alien_height = 50

        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
