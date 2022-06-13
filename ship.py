import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's y value, not the rect
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_vertical
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_vertical

        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_horizontal
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_horizontal
        # Update rect object from self.y
        self.rect.y = self.y

        # Update rect object fron self.x
        self.rect.x = self.x
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)