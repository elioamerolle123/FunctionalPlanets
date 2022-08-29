
"""
    1. SET UP THE PHYSICS INSIDE THE CLASS (BIG ERRRORRR NEED TO REFIGURE
    OUT THE MATH YOU CANNOT ASSUME CIRCULAR MOTION ---> ALL THE FORMULAS HAVE GONE TO SHIT)
    2. GET THE SUMATION OF FORCES TO WORK
    3. Colision detection and identification of pairs
    4. Functions necissary to create new planets resulting from the colided ones
    5. ADD THE COLOR SCHEME WE WANT

    ^^^^^DONE^^^^^

    6. Add vectors
    7. zoom and push screen
    8. fail safe the colors

"""


import math
import pygame
import copy
from Planet import Planet

from Vector import Arrow

from Funcs import Funcs

pygame.init()

screen = pygame.display.set_mode([1250, 750])

testSpeed = 0.005


#         (x, y, v, r, density, k, surface)
p0 = Planet(200, 400, [0, 0], 30, 100, testSpeed, screen)
p1 = Planet(900, 500, [0, 0], 40, 120, testSpeed, screen)
p2 = Planet(100, -100, [75, 0], 10, 50, testSpeed, screen)


p3 = Planet(700, 500, [-300, 0], 8, 50, testSpeed, screen)
p4 = Planet(655, 600, [-300, 0], 10, 50, testSpeed, screen)
p5 = Planet(800, 200, [-300, 0], 15, 50, testSpeed, screen)



planets = [p0, p1]

velVects = [Arrow(screen) for i in range(len(planets))]

forceVects = [Arrow(screen) for i in range(len(planets))]


forces = [[0,0] for i in range(len(planets))]


counter = 0

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((50, 50, 50))

    #CODE GO BELOW

    # Rendering the planets
    for i in range(len(planets)):

        planets[i].render()
        #velVects[i].render(planets[i].x, planets[i].y, copy.deepcopy(planets[i].vel), 9)
        
        
        forceVects[i].render(planets[i].x, planets[i].y, (forces[i]), 11)
        print(forces[i])

    

    collidedPs = []
    

    # Sumation of the force vectors
    for i in range(len(planets)):
        direction = [0,0]


        for e in range(len(planets)):
            if i != e:
                direction[0] = planets[e].x - planets[i].x
                direction[1] = planets[e].y - planets[i].y

                dis = math.sqrt(direction[0] ** 2 + direction[1] ** 2)

                Fmag = (planets[e].mass * planets[i].mass)/(dis ** 2)

                if dis < planets[e].r + planets[i].r:
                    if not (planets[e] in collidedPs and planets[i] in collidedPs):
                        collidedPs.append(planets[e])
                        collidedPs.append(planets[i])
                    

                forces[i] = Funcs.vectorAdd(forces[i], Funcs.scalarMultiplier(Fmag, Funcs.normalizer(direction)))

    Acc = True

    if len(planets) == 1:
        Acc = False


    for i in range(len(planets)):
        planets[i].gravity(forces[i], Acc)


    while len(collidedPs) > 0:
        rat = (collidedPs[0].mass/(collidedPs[0].mass + collidedPs[1].mass))

        collidedPs[0].vel = Funcs.vectorAdd(Funcs.scalarMultiplier(rat, collidedPs[0].vel), Funcs.scalarMultiplier(1 - rat, collidedPs[1].vel))

        collidedPs[0].x = collidedPs[0].x * rat + collidedPs[1].x * (1 - rat)
        collidedPs[0].y = collidedPs[0].y * rat + collidedPs[1].y * (1 - rat)


        collidedPs[0].density = collidedPs[0].density * (rat) + collidedPs[1].density * (1 - rat)
        collidedPs[0].mass = collidedPs[0].mass + collidedPs[1].mass

        collidedPs[0].r = ((3 * collidedPs[0].mass)/(4 * math.pi * collidedPs[0].density)) ** (1/3)


        planets.remove(collidedPs[1])
        collidedPs.remove(collidedPs[1])
        collidedPs.remove(collidedPs[0])


        
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()