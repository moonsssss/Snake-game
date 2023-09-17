"""
Starter code for retro snake game.
Notes: You can decrease and increase the snake game map manualey for bigger or smaller play 
"""
import pygame
from sys import exit
import random
#reset = pygame.image.load("Snake\images\reset-button-computer-icons-clip-art-restart-d431af2a2c2542d3a09a1e271fd20eda.png")

# The code for the snake and its behavior.
# The snake is made up of it's length, a list of the coordinates
# of its body blocks, and the direction it's heading in.
class Snake(object):
    def __init__(self):
        # positions is a list tracking the coordinates (x, y) of all the
        # body blocks of the snake. New blocks are added to the end.

        # 1) Set up the snake's position list
        x = SCREEN_WIDTH/2 - GRID_SIZE/2
        y = SCREEN_HEIGHT/2 - GRID_SIZE/2
        self.positions_list = [(x,y)]                                                
        # 2) Set up the snake's length
        self.length = 2
        # 3) Set up the snake's direction 
        self.direction = RIGHT
        # 4) Set up the snake's color
        self.color = (69, 114, 231)
        # 5) Calling the snake
        self.draw(background)
        # 6) Senting up snake score
        self.snakescore = 0

    # This returns the coordinate of the snake's head (first square)
    def get_head(self):
        return self.positions_list[0]
        

    # `direction` represents one of the four directions the snake can turn in
    def turn(self, user_input):
        # If the snake is moving UP, we cannot turn DOWN
        if self.direction == UP:
            if user_input != DOWN:
                self.direction = user_input

        # If the snake is moving DOWN, we cannot turn UP
        elif self.direction == DOWN:
            if user_input != UP:
                self.direction = user_input

        # If the snake is moving LEFT, we cannot turn RIGHT
        elif self.direction == LEFT:
            if user_input != RIGHT:
                self.direction = user_input

        # If the snake is moving RIGHT, we cannot turn LEFT
        elif self.direction == RIGHT:
            if user_input != LEFT:
                self.direction = user_input
       


    # This is the function which moves the snake!
    def move(self):
        # Useful command to make a new body part:
        oldhead = self.get_head()
        head_x_coord = oldhead[0]
        head_y_coord = oldhead[1]
        snake_x_direction = self.direction[0]
        snake_y_direction = self.direction[1]
        newhead = ((head_x_coord + snake_x_direction * GRID_SIZE), (head_y_coord + snake_y_direction * GRID_SIZE))
        
        # TODO Check to see if the snake move is valid
        # - If the move is valid, allow the move
        # - If not, end the game.
        if (self.outOfBounds() == True):
            self.gameover()
        elif len(self.positions_list) > 2 and newhead in self.positions_list[2:]:
            self.gameover()
        else: 
            self.positions_list.insert(0, newhead)
        
            if len(self.positions_list) > self.length: 
                self.positions_list.pop()
            
    # This function will be called when the code determines the game over
    # You can have a gameover screen appear and inform the player how to play again
    def gameover(self):
        self.direction = GAMEOVER 
        font = pygame.font.SysFont("yugothicmedium", 60)
        gameover_text = font.render("GAMEOVER",False, (204, 64, 0))
        gameover_text_rect = gameover_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        background.blit(gameover_text, gameover_text_rect)
        #reset.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
     

    # This function is called when the player restarts the game.
    # It should reset the snake back to it's initial conditions.
    def reset(self):
        pass # remove this line once you add code!

    # Provided: Draws all of the snake's body parts
    def draw(self, background):
        for position in self.positions_list:
            block = pygame.Rect(position[0], position[1], GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(background, self.color, block)
            pygame.draw.rect(background, (0, 0, 0), block, 1)

    # This is a helper function which will check whether the snake is out of bounds
    # Returns True if out of bounds, False if not.
    def outOfBounds(self):
        head = self.get_head()
        head_x = head[0]
        head_y = head[1]
        if head_x < 0:
            return True
        if head_y < 0:
            return True
        if SCREEN_WIDTH < head_x:
            return True
        if SCREEN_HEIGHT < head_y:
            return True
        return False


# The food (apple). Only implement after you've made the snake
class Food(object):
    # Function to initialize (set up the food)
    # Python automatically calls this function when you create a food object. e.g. food = Food()
    def __init__(self):
        # TODO
        # Format: self.variable_name = value
        # 1) Set up the apple's position list
        self.place = (NUM_GRIDS_X//2 * GRID_SIZE ,NUM_GRIDS_Y//2 * GRID_SIZE)
        # 2) Set up the apple's color
        self.color = (231,71,29)
        

    # Function to randomize the position of the food/apple when it's spawned
    def randomize_position(self):
       x = random.randint(0, NUM_GRIDS_X - 1) * GRID_SIZE
       y = random.randint(0, NUM_GRIDS_Y - 1) * GRID_SIZE
       self.place = (x, y)
       

    # This function is responsible for actually drawing the apple onto the background provided!
    def draw(self, background):
        block = pygame.Rect(self.place[0], self.place[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(background, self.color, block)
        pygame.draw.rect(background, (0, 0, 0), block, 1)



# USEFUL CONSTANTS
# Screen constants
SCREEN_WIDTH = 680
SCREEN_HEIGHT = 600 

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
            color_1 = (162, 209, 73)
            color_2 = (170, 215, 81)
            if ((x + y) % 2 == 1):
                pygame.draw.rect(background, color_1, next_rect)
            else:
                pygame.draw.rect(background, color_2, next_rect)

pygame.init() 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# creating a name for your game
pygame.display.set_caption("Snake Game!")
# creating a clock/ framerate
clock = pygame.time.Clock()
#Changing the app icon
icon = pygame.image.load("Snake\images\Snake pic.jpeg")
pygame.display.set_icon(icon)

# Create a background surface!
surface_width_height = screen.get_size()
background = pygame.Surface(surface_width_height)

snake = Snake()
food = Food()
while True:
    # Event loop (checking for player input)
    for event in pygame.event.get():
        # gets all of the "events" in pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                snake.turn(UP)
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                snake.turn(DOWN)
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                snake.turn(LEFT)
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                snake.turn(RIGHT)

            
    # Draw all of our elements! (like the draw function in trinket)
    drawGrid(background)
    if snake.get_head() == food.place:
        snake.length =  snake.length + 1 
        snake.snakescore = snake.snakescore + 1 
        food.randomize_position()
    food.draw(background)
    snake.move()
    fonts = pygame.font.Font(pygame.font.get_default_font(),20)
    text = fonts.render(f"Score: {snake.snakescore}", False, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (50, 50)
    background.blit(text, textRect)
    snake.draw(background)
    screen.blit(background, (0, 0))
    pygame.display.update()  # This will update the screen to the player!
    clock.tick(5) # like our framerate in trinket! tells pygame to to do this while true loop 60 times per second
