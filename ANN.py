import numpy
import random
import copy
import matplotlib as plt
import math

def MatrixCreate(rows, cols):
    matrix = numpy.zeros(shape=(rows, cols))
    return matrix
    
def computePosition(numNeurons):
    neuronPositions=MatrixCreate(2, numNeurons)
    angle = 0.0 
    angleUpdate = 2 * math.pi / numNeurons 
    for i in range(numNeurons):
        neuronPositions[0,i] = math.sin(angle)
        neuronPositions[1,i] = math.cos(angle)
        angle = angle + angleUpdate
    
    return neuronPositions

numNeurons = 10
        
neuronValues=MatrixCreate(50,numNeurons)
for y in range(len(neuronValues[0])):
    neuronValues[0][y] = random.random()
       
np = computePosition(numNeurons)
print(np) 

plt.pyplot.plot(np[0], np[1], 'ko', markerfacecolor=[1,1,1], markersize=18)
plt.pyplot.axis([-1, 1, -1, 1])
plt.pyplot.show()
