
import pygame
import math

from Funcs import Funcs

class Planet:
    def __init__(self, x, y, vel, r, density, k, surface):
        self.x = x
        self.y  = y
        self.vel  = vel
        self.r  = r
        self.density = density
        self.k = k
        self.surface = surface

        self.mass = (4/3) * math.pi * (float(r) ** 3) * float(density)

    def render(self):

        pygame.draw.circle(self.surface, (100 - 0.5 * self.r, 100 - 0.5 * self.density, 255 - (self.r + self.density)), (self.x, self.y), self.r)

    def gravity(self, fors, Acc):

        accMag = math.sqrt(fors[0] ** 2 + fors[1] ** 2)/self.mass

        accVect = [0,0]

        if Acc:
            accVect = Funcs.scalarMultiplier(accMag, Funcs.normalizer(fors))
        

        self.vel[0] += accVect[0] * self.k
        self.vel[1] += accVect[1] * self.k

        self.x += self.vel[0] * self.k
        self.y += self.vel[1] * self.k

        


