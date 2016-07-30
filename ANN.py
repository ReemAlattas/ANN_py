import numpy
import random
import copy
import matplotlib as plt
import math

def MatrixCreate(rows, cols):
    matrix = numpy.zeros(shape=(rows, cols))
    return matrix
    
def computePosition(numNeurons):
    neuronPositions=MatrixCreate(2,10)
    angle = 0.0 
    angleUpdate = 2 * math.pi /numNeurons 
    for i in range(0,numNeurons):
        x = math.sin(angle)
        y = math.cos(angle)
        angle = angle + angleUpdate
    
    return neuronPositions
    
neuronValues=MatrixCreate(50,10)
for y in range(len(neuronValues[0])):
    neuronValues[0][y] = random.random()
    
print(neuronValues)



