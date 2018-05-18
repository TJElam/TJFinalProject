# Tech With Tim https://www.youtube.com/watch?v=PjgLeP0G5Yw&list=PLzMcBGfZo4-nh5Txa7ypUiv_4EVq4dgKc
# imports
import pygame

class Player(pygame.sprite.Sprite):
    """
    This class represent the player image
    and has the player actions.
    """
    direction = 'right'
    def __init__(self, color, width, height, x, y):
        # Pygame constructor
        pygame.sprite.Sprite.__init__(self)

        # Init. variables
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y 

        # Create sprite
        self.image = pygame.Surface([width, height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

    def draw(self, screen):
        # Draw player on the screen
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height], 0)

    def move(self, speed, walls):
        # Move the player
        if self.direction == 'up':
            self.y -= speed
        elif self.direction == 'down':
            self.y += speed
        elif self.direction == 'left':
            self.x -= speed
        elif self.direction == 'right':  
            self.x += speed