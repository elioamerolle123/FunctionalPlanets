import math
import pygame

from Funcs import Funcs

class Arrow:
    def __init__(self, window):
        
        self.window = window


    def render(self, x, y, direction, reduct):
        width = 4
        ArrPlus = (1/4) * width
        Mag = math.sqrt(direction[0] ** 2 + direction[1] ** 2)/reduct

        theta = math.asin(Funcs.normalizerVect(direction)[1])

        if Funcs.normalizerVect(direction)[0] < 0:
            theta = math.pi - theta

        P = [Funcs.rot(theta, [0, -width/2]), Funcs.rot(theta, [0, width/2]), Funcs.rot(theta, [(Mag - 5), width/2]), Funcs.rot(theta, [(Mag - 5), width/2 + ArrPlus]), Funcs.rot(theta, [Mag, 0]), Funcs.rot(theta, [(Mag - 5), - width/2 - ArrPlus]), Funcs.rot(theta, [(Mag - 5), - width/2])]
        
        
        #                                R  G  B     Cords                                             A               B                                   Point           B ref            A ref
        pygame.draw.polygon(self.window, (75, 75, 255), ((x + P[0][0], y + P[0][1]), (x + P[1][0], y + P[1][1]), (x + P[2][0], y + P[2][1]), (x + P[3][0], y + P[3][1]), (x + P[4][0], y + P[4][1]), (x + P[5][0], y + P[5][1]), (x + P[6][0], y + P[6][1])))