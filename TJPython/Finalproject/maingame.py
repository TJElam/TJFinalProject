# Tech With Tim https://www.youtube.com/watch?v=PjgLeP0G5Yw&list=PLzMcBGfZo4-nh5Txa7ypUiv_4EVq4dgKc
# Imports
import pygame
import sys
import player
import room

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)

# Global variables
S_WIDTH = 800
S_HEIGHT = 800
FPS = 60
# player speed
SPEED = 2
WALLS = pygame.sprite.Group()

# Initialization 
pygame.init()
screen = pygame.display.set_mode([S_WIDTH, S_HEIGHT])
pygame.display.set_caption("Py-Man Alpha")
clock = pygame.time.Clock()

# Add walls to WALLS var.
wall = room.Wall(0, 600, 1000, 30, black, screen)
WALLS.add(wall)

# Main class
class Main(object):
    """
    This is main class of 
    the program. Here, the menu 
    will be showed and player 
    can start game, load, access 
    options or quit.
    """
    def __init__(self, screen):
        self.screen = screen

        self.menu()

    def menu(self):
        # Show menu
        pass

    def load(self):
        # Load game
        pass

    def options(self):
        # Show options
        pass

    def quit(self):
        pygame.quit()
        sys.exit()

# Game class
class Game(object):
    """
    This is main class of game.
    All game events will happen here.
    """
    Player = player.Player(blue, 50, 50, 0, 0) 
    def __init__(self, screen, running):
        self.screen = screen
        self.running = running

        self.run()

    def run(self):
        while self.running:
            # Events
            for event in pygame.event.get():
                # If user hits 'x'
                if event.type == pygame.QUIT:
                    self.running = False
                # Keyborad events
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.Player.direction = 'up'
                    elif event.key == pygame.K_DOWN:
                        self.Player.direction = 'down'
                    elif event.key == pygame.K_LEFT:
                        self.Player.direction = 'left'
                    elif event.key == pygame.K_RIGHT:
                        self.Player.direction = 'right'
                    elif event.key == pygame.K_p:
                        self.Player.direction = 'pause'
            # Clear screen
            self.screen.fill(white)

            #Draw
            self.Player.move(SPEED, WALLS)
            self.Player.draw(self.screen)
            for wall in WALLS:
                wall.draw()

            # Set clock
            clock.tick(60)

            # Update screen
            pygame.display.flip()

        # End of game
        pygame.quit()
        sys.exit()

# Tests
game = Game(screen, True)