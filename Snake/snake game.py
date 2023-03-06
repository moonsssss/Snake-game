# import pygame
# #from sys import exit

# pygame.init()
# screen = pygame.display.set_mode((800, 400))

# pygame.display.set_caption("Snake 101")

# background = pygame.image.load("Snake\images\Snake Game background.jpg")

# while True: 
#    for event in pygame.event.get():  
#        if event.type == pygame.QUIT:
#            pygame.quit()
#            #exit()
#     #screen.blit(background, (0,0))

#    pygame.display.update()  



"""
Ulo Freitas pygame starter. Creating a blank screen.
"""
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
# creating a name for your game
pygame.display.set_caption("Ulo's Super Cool Game!!")

while True:
   # Event loop (checking for player input)
   for event in pygame.event.get():
       # gets all of the "events" in pygame
       if event.type == pygame.QUIT:
           pygame.quit()
           exit()

   # Draw all of our elements! (like the draw function in trinket)
   pygame.display.update()  # This will update the screen to the player!
