import math

matrix = [[1, 2], 
        [3, 4]]
numOfHs = 0
numOfVs = 0

def Transformations(tList):
    numOfHs = tList.count("H")
    numOfVs = tList.count("V")
    if numOfHs % 2 != 0:
        matrix.reverse()
    if numOfVs %2 != 0:
        matrix[0].reverse()
        matrix[1].reverse()

Transformations(["H", "V"])

print("%s %s" % (matrix[0][0], matrix[0][1]))
print("%s %s" % (matrix[1][0], matrix[1][1]))