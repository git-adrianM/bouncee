from turtle import shape
import pygame
pygame.mixer.init()

sound = pygame.mixer.Sound("Clack.wav")

class Blocks:

    def __init__(self,BlockColor, screen, x, w, v, m) -> None:
        self.screen =  screen
        self.BlockColor = BlockColor
        self.m = m
        self.w = w
        self.y = (screen.get_height()//2) - w 
        self.v = v
        self.rea = pygame.Rect((x, self.y), (w, w))

    def hitWall(self):
        return (self.rea.x < 0)

    def collide(self,other):
        return not (self.rea.x + self.w < other.rea.x or self.rea.x > other.rea.x + other.w)

    def bounce(self, other):
        pygame.mixer.Sound.play(sound)
        sumM = self.m + other.m
        newV = ((self.m-other.m)/sumM) * self.v
        newV += ((2 * other.m )/ sumM) * other.v
        return newV

    def show(self):
        pygame.draw.rect(self.screen, self.BlockColor, (self.rea))
        pygame.display.update()

    def update(self):
        self.rea.move_ip(self.v, 0)
