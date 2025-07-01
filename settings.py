# settings.py

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):  # ✅ Corrected init
        # Screen settings
        self.screen_width = 800
        self.screen_height = 800  # Increased vertical space
        self.bg_color = (30, 30, 30)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 0.3  # Slower horizontal speed
        self.fleet_drop_speed = 5  # Slower downward speed
        self.fleet_direction = 1

        # Speedup scale
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.3
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
