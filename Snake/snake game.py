"""
Starter code for retro snake game.
"""
import pygame
from sys import exit
import random


# The code for the snake and its behavior.
# The snake is made up of it's length, a list of the coordinates
# of its body blocks, and the direction it's heading in.
class Snake(object):
    def __init__(self):
        # positions is a list tracking the coordinates (x, y) of all the
        # body blocks of the snake. New blocks are added to the end.

        # TODO
        # Format: self.variable_name = value
        # 1) Set up the snake's position list
        # 2) Set up the snake's length
        # 3) Set up the snake's direction
        # 4) Set up the snake's color
        pass # remove this line once you add code!

    # This returns the coordinate of the snake's head (first square)
    def get_head(self):
        pass # remove this line once you add code!

    # `direction` represents one of the four directions the snake can turn in
    def turn(self, direction):
        # If the snake is moving UP, we cannot turn DOWN

        # If the snake is moving DOWN, we cannot turn UP

        # If the snake is moving LEFT, we cannot turn RIGHT

        # If the snake is moving RIGHT, we cannot turn LEFT
        pass # remove this line once you add code!


    # This is the function which moves the snake!
    def move(self):
        # Useful command to make a new body part:
        # new = ((head_x_coord + snake_x_direction * GRID_SIZE), (head_y_coord + snake_y_direction * GRID_SIZE))

        # TODO Check to see if the snake move is valid
        # - If the move is valid, allow the move
        # - If not, end the game.
        pass # remove this line once you add code!


    # This function will be called when the code determines the game over
    # You can have a gameover screen appear and inform the player how to play again
    def gameover(self):
        pass # remove this line once you add code!

    # This function is called when the player restarts the game.
    # It should reset the snake back to it's initial conditions.
    def reset(self):
        pass # remove this line once you add code!

    # Provided: Draws all of the snake's body parts
    def draw(self, background):
        # Go through all of the cells in the position list and draw them!
        pass # remove this line once you add code!

    # This is a helper function which will check whether the snake is out of bounds
    # Returns True if out of bounds, False if not.
    def outOfBounds(self):
        pass # remove this line once you add code!


# The food (apple). Only implement after you've made the snake
class Food(object):
    # Function to initialize (set up the food)
    # Python automatically calls this function when you create a food object. e.g. food = Food()
    def __init__(self):
        # TODO
        # Format: self.variable_name = value
        # 1) Set up the apple's position list
        # 2) Set up the apple's color
        pass # remove this line once you add code!

    # Function to randomize the position of the food/apple when it's spawned
    def randomize_position(self):
        pass # remove this line once you add code!

    # This function is responsible for actually drawing the apple onto the background provided!
    def draw(self, background):
        pass # remove this line once you add code!

# USEFUL CONSTANTS
# Screen constants
SCREEN_WIDTH = 40 # TODO set your screen width
SCREEN_HEIGHT = 40 # TODO set your screen height

# Grid constants
GRID_SIZE = 40
NUM_GRIDS_X = SCREEN_WIDTH / GRID_SIZE
NUM_GRIDS_Y = SCREEN_HEIGHT / GRID_SIZE

# Movement in terms of grid cells: (x, y)
# E.g. UP can be used
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
GAMEOVER = (0, 0)

# Provided: Function which draws the playing grid.
def drawGrid(background):
    for x in range(int(NUM_GRIDS_X)):
        for y in range(int (NUM_GRIDS_Y)):
            rect_x = x * GRID_SIZE
            rect_y = y * GRID_SIZE
            next_rect = pygame.Rect(rect_x, rect_y, GRID_SIZE, GRID_SIZE)
            # TODO: Add your own colors to the grids!
            color_1 = (0, 0, 0)
            color_2 = (255, 255, 255)
            if ((x + y) % 2 == 1):
                pygame.draw.rect(background, color_1, next_rect)
            else:
                pygame.draw.rect(background, color_2, next_rect)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# creating a name for your game
pygame.display.set_caption("TODO: Add your own title here!")
# creating a clock/ framerate
clock = pygame.time.Clock()

# Create a background surface!
surface_width_height = screen.get_size()
background = pygame.Surface(surface_width_height)


while True:
    # Event loop (checking for player input)
    for event in pygame.event.get():
        # gets all of the "events" in pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Draw all of our elements! (like the draw function in trinket)
    drawGrid(background)
    screen.blit(background, (0, 0))
    pygame.display.update()  # This will update the screen to the player!
    clock.tick(5) # like our framerate in trinket! tells pygame to to do this while true loop 60 times per second