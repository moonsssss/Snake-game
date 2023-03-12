import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((548, 483))

pygame.display.set_caption("Snake 101")

background = pygame.image.load("Snake\images\Snake Game background.jpg")
apple = pygame.image.load("Snake\images\—Pngtree—fruit cartoon fruit cartoon red_3806661.png").convert_alpha()
apple_rec = apple.get_rect(midbottom = (328, 325))
while True: 
   for event in pygame.event.get():  
       if event.type == pygame.QUIT:
           pygame.quit()
           exit()
    
   screen.blit(background, (0,0))
   screen.blit(apple, apple_rec)
   pygame.display.update()  