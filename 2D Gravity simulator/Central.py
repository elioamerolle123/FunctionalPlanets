
import math
import pygame
import copy
import time


from pygame.locals import *


from Planet import Planet

from Vector import Arrow

from Funcs import Funcs

pygame.init()

screen = pygame.display.set_mode([1250, 750])

testSpeed = 0.005


# Here you can initialize planets (you still need to ADD them TO the LIST though in LINE 35)
#         (x Pos, y Pos, v initial, radius, density, speed of sim)
p0 = Planet(200, 400, [0, 0], 30, 100, testSpeed, screen)
p1 = Planet(900, 500, [0, 0], 40, 120, testSpeed, screen)
p2 = Planet(100, -100, [75, 0], 10, 50, testSpeed, screen)


p3 = Planet(700, 500, [0, 300], 8, 50, testSpeed, screen)
p4 = Planet(655, 600, [-300, 0], 10, 50, testSpeed, screen)
p5 = Planet(800, 200, [-300, 100], 15, 50, testSpeed, screen)
p6 = Planet(900, 250, [400, 200], 4, 50, testSpeed, screen)

p7 = Planet(900, 250, [400, 200], 50, 50, testSpeed, screen)


# list of planets (IF YOU WANT ANOTHER PLANET OR IF YOU WANT TO ADD ONE YOU NEED TO CHANGE THE LIST)
planets = [p0, p1, p3, p4, p5, p6]


velVects = [Arrow(screen) for i in range(len(planets))]

forceVects = [Arrow(screen) for i in range(len(planets))]


forces = [[0,0] for i in range(len(planets))]

forcesForVect = [[0,0] for i in range(len(planets))]

counter = 0

prevVal = False

Acc = True

running = True


while running:

    grav = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.fill((50, 50, 50))

    #CODE GO BELOW
    collidedPs = []


    #Sums the forces for each planet to find the net force (if you want to look at the actual function check the class Funcs)
    Funcs.sumForce(planets, forces, collidedPs)
                
        # for loop to copy whats in forces (copy decopy failed and other methds failed beacuse it is 2D)
    for i in range(len(forces)):
        forcesForVect[i] = [0, 0]
        forcesForVect[i][0] = forces[i][0]
        forcesForVect[i][1] = forces[i][1]

        
        # If there is only one planet then there is no acc. (fix for error when force = 0)
     
    
    if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pressed()[0] != prevVal:
        counter += 1

        prevVal = pygame.mouse.get_pressed()[0]


    if pygame.mouse.get_pressed()[0] == False:
        prevVal = False

    
    moveVect = pygame.mouse.get_rel()

    
    if bool(counter%2):
        forces = [[0,0] for i in range(len(planets))]
        grav = False        

    else:
        moveVect = (0, 0)


    for i in planets:
        i.x += moveVect[0]
        i.y += moveVect[1]

################################################################################################
    
    if len(planets) == 1:
        Acc = False

    if grav:
        for i in range(len(planets)):

            planets[i].gravity(Acc, forces[i])
            

    Funcs.colisionWork(planets, collidedPs)


    #for loop necissary for rendering everything
    Funcs.renderSystem(planets, forceVects, forcesForVect, velVects)




    pygame.display.flip()

pygame.quit()
