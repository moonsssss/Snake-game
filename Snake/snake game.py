import pygame
import pygame.locals
from sys import exit

pygame.init()
screen = pygame.display.set_mode((548, 483))

pygame.display.set_caption("Snake 101")
clock = pygame.time.Clock()
background = pygame.image.load("Snake\images\Snake Game background.jpg")
apple = pygame.image.load("Snake\images\Apple.png").convert_alpha()
apple = pygame.transform.scale(apple, (32, 32))
apple_rec = apple.get_rect(midbottom = (328, 325))
while True: 
   for event in pygame.event.get():  
       if event.type == pygame.QUIT:
           pygame.quit()
           exit()
    
   screen.blit(background, (0,0))
   screen.blit(apple, apple_rec)
   print(apple_rec.x)
   keys = pygame.key.get_pressed()
   if keys[pygame.K_LEFT]:
    apple_rec.x = apple_rec.x - 1
   pygame.display.update()
   clock.tick(60)