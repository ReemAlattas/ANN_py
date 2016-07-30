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
    
def plotSynapses(neuronPositions, synapses):
    #print(len(neuronPositions[0]))
    for i in range(len(neuronPositions[0])):
        for j in range(len(neuronPositions[0])):
            if (synapses [i][j] < 0):
                plt.pyplot.plot([neuronPositions[0,i],neuronPositions[0,j]],[neuronPositions[1,i],neuronPositions[1,j]], color=[0.8,0.8,0.8])
            else:
                plt.pyplot.plot([neuronPositions[0,i],neuronPositions[0,j]],[neuronPositions[1,i],neuronPositions[1,j]], color=[0,0,0])
            
numNeurons = 10
        
neuronValues = MatrixCreate(50,numNeurons)
for y in range(len(neuronValues[0])):
    neuronValues[0][y] = random.random()
       
np = computePosition(numNeurons)
print(np) 

plt.pyplot.plot(np[0], np[1], 'ko', markerfacecolor=[1,1,1], markersize=18)
plt.pyplot.axis([-1, 1, -1, 1])
plt.pyplot.show()

synapses = MatrixCreate(numNeurons,numNeurons)
synapses = [[random.uniform(-1, 1) for y in range(len(synapses[x]))] for x in range(len(synapses))]
print(synapses)

plotSynapses(np, synapses)
