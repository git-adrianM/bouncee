import time
import pygame
from pygame import mixer
from Block import Blocks

sound = pygame.mixer.Sound("Clack.wav")

pygame.mixer.init()
pygame.init()

WIDTH, HEIGHT = 1200, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_over = False

GREY = (150, 150, 150)
RED = (255,0,0)
BLUE = (0,0,255)
print(screen)
m2 = pow(100, 1)
Block1 = Blocks(RED, screen, 200, 50, 0, 1)
Block2 = Blocks(BLUE, screen, 500, 50, -1, m2)

count = 0
while not game_over:

    #screen.fill(GREY, (0, screen.get_height()//2, screen.get_width(), screen.get_height()//2))
    screen.fill((255,255,255), (0,0, screen.get_width(), screen.get_height()//2))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game_over = True

    if Block1.hitWall():
        pygame.mixer.Sound.play(sound)
        count += 1
        Block1.v *= -1
        print(count)
        
    if Block2.hitWall():
        pygame.mixer.Sound.play(sound)
        count += 1
        Block2.v *= -1
        print(count)

    if Block1.collide(Block2):
        count += 1
        print(count)
        v1 = Block1.bounce(Block2)
        v2 = Block2.bounce(Block1)
        Block1.v = v1
        Block2.v = v2

    Block1.show()
    Block2.show()
    Block1.update()
    Block2.update()


pygame.quit()