import pygame
from pygame.font import Font

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)

        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        score_str = f"Score: {self.stats.score}"
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = 20
        self.score_rect.right = self.screen_rect.right - 20

    def prep_high_score(self):
        high_score_str = f"High Score: {self.stats.high_score}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.top = self.score_rect.bottom + 10
        self.high_score_rect.right = self.screen_rect.right - 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

