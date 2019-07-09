class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """initialise the game's static settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230) # light grey

        # Ship settings
        self.ship_limit = 3
        self.ship_width = 50
        self.ship_height = 60

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_width = 80
        self.alien_height = 50
        self.fleet_drop_speed = 10
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        self.ship_speed = 1.5
        self.alien_speed = 0.8
        self.bullet_speed = 1.5

        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 20

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale