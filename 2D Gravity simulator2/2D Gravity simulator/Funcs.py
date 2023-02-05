import math
import copy


class Funcs:

    def mag(v):
        return math.sqrt((v[0] ** 2) + (v[1] ** 2))

    def normalizerVect(v):
        if not((v[0] ** 2) + (v[1] ** 2) == 0):
            k = 1/math.sqrt((v[0] ** 2) + (v[1] ** 2))
        else:
            k = 0

        for i in range(2):
            v[i] = k * v[i]

        return v

    def normalizer(v):
    
        k = 1/math.sqrt((v[0] ** 2) + (v[1] ** 2))

        for i in range(2):
            v[i] = k * v[i]

        return v

    def scalarMultiplier(k, v):
        for i in range(len(v)):
            v[i] = k * v[i]

        return v

    def vectorAdd(v1, v2):
        r = [0 for i in range(len(v1))]

        for i in range(len(v1)):
            r[i] = v1[i] + v2[i]

        return r

    def avg(a, b):
        return (a + b)/2

    def mM(mat1, mat2):
        height1 = len(mat1)
        width1 = len(mat1[0])
        width2 = 1


        matMul = [[0 for i in range(width2)] for e in range(height1)]


        for i in range(height1):
            for e in range(width2):
                
                sum = 0

                for j in range(width1):
                    sum += mat1[i][j] * mat2[j]

                matMul[i][e] = sum
        
        columVect = [0 for i in range(height1)]

        for i in range(height1):
            columVect[i] = matMul[i][0]

        return columVect


    def rot(theta, vect):
        rotMat = [[math.cos(theta), -math.sin(theta)],[math.sin(theta), math.cos(theta)]]
        return Funcs.mM(rotMat, vect)

    def sumForce(planets, forces, collidedPs):
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

    def colisionWork(planets, collidedPs):
        
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
            
    def renderSystem(planets, forceVects, forcesForVect, velVects):
        for i in range(len(planets)):

            planets[i].render()
            velVects[i].render(planets[i].x, planets[i].y, copy.deepcopy(planets[i].vel), 9, 25, 100, 255)


            forceVects[i].render(planets[i].x, planets[i].y, (forcesForVect[i]), 10000000, 250, 150, 25)
              
