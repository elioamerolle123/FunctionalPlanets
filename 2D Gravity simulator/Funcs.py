import math

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

        
          