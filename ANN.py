import numpy
import random
import copy
import matplotlib as plt

def MatrixCreate(rows, cols):
    # matrix = [[0 for y in range(cols)] for x in range(rows)]
    matrix = numpy.zeros(shape=(rows, cols))
    return matrix
    
def MatrixRandomize(v):
    random_m = [[random.random() for y in range(len(v[x]))] for x in range(len(v))]
    return random_m
    
def Fitness(v):
    mean_val = numpy.mean(v)
    return mean_val
    
def MatrixPerturb(p, prob):
    c = copy.deepcopy(p)
    #print(p)
    #print(c)
    for x in range(len(c)):
        for y in range(len(c[x])):
            if prob > random.random():
                c[x][y] = random.random()
    return c
    
def PlotVectorAsLine(fits):
    plt.pyplot.plot(fits[0])
    plt.pyplot.xlabel('Generation')
    plt.pyplot.ylabel('Fitness')
    plt.pyplot.show()
    

def HillClimber():
    for i in range(5):    
        parent = MatrixCreate(1, 50)
        parent = MatrixRandomize(parent)
        parentFitness = Fitness(parent)
        
        fits = MatrixCreate(1, 5000)
        Genes = MatrixCreate(50, 5000)
        
        for currentGeneration in range(5000):
            #print currentGeneration, parentFitness
            fits[0][currentGeneration] = parentFitness
            child = MatrixPerturb(parent, 0.05) 
            childFitness = Fitness(child) 
            if childFitness > parentFitness:
                parent = child 
                parentFitness = childFitness
            for idx, val in enumerate(parent[0]):
                Genes[idx][currentGeneration] = val
                      
        #print(Genes)            
        #PlotVectorAsLine(fits)
    plt.pyplot.imshow(Genes, cmap=plt.cm.gray, aspect='auto', interpolation='nearest')
    plt.pyplot.show()
        
#HillClimber()
neuronValues = MatrixCreate(50, 10)
for y in range(len(neuronValues[0])):
    neuronValues[0][y] = random.random()
    
print(neuronValues)