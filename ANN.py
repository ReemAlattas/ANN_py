import numpy
import random
import copy
import matplotlib as plt
import math

numNeurons = 10

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
            w = int(10*abs(synapses[i][j]))+1
            if (synapses [i][j] < 0):
                plt.pyplot.plot([neuronPositions[0,i],neuronPositions[0,j]],[neuronPositions[1,i],neuronPositions[1,j]], color=[0.8,0.8,0.8], linewidth= w)
            else:
                plt.pyplot.plot([neuronPositions[0,i],neuronPositions[0,j]],[neuronPositions[1,i],neuronPositions[1,j]], color=[0,0,0], linewidth= w)
            
def Update (neuronValues, synapses, i):
    sum = 0 
    for j in range(numNeurons):
        for k in range(numNeurons):
            temp = neuronValues[i-1][k] * synapses[j][k]
            sum = sum + temp
        if (sum < 0):
            sum = 0
        if (sum > 1):
            sum = 1
        neuronValues[i][j] = sum        
    return neuronValues


        
neuronValues = MatrixCreate(50,numNeurons)
for y in range(len(neuronValues[0])):
    neuronValues[0][y] = random.random()
       
np = computePosition(numNeurons)
print(np) 

#plt.pyplot.plot(np[0], np[1], 'ko', markerfacecolor=[1,1,1], markersize=18)
#plt.pyplot.axis([-1, 1, -1, 1])
#plt.pyplot.show()

synapses = MatrixCreate(numNeurons,numNeurons)
synapses = [[random.uniform(-1, 1) for y in range(len(synapses[x]))] for x in range(len(synapses))]
print(synapses)

for i in range(1, 50):
    neuronValues = Update (neuronValues, synapses, i)
print (neuronValues)

plt.pyplot.xlabel('Neuron')
plt.pyplot.ylabel('Time Step')
plt.pyplot.imshow(neuronValues, cmap=plt.cm.gray, aspect='auto', interpolation='nearest')
plt.pyplot.show()

#plotSynapses(np, synapses)
