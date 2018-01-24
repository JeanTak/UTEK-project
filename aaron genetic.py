POPULATION = 50
N=3
import random

def randomGeneration(n):
    #generate a random generation with N KEYS
    #output: list[list[int]]
    generation = []
    for i in range(POPULATION):
        individual = []
        for j in range(n):
            individual.append(random.randint(0,25))
        generation.append(individual)
    return generation

def getDNA(indi):
    #get the DNA of the individual
    #DNA is a list of size 5*N, in binary
    #ex. [0,1,0,1,0,0,0,0,0,0,0,1,1,1,1] represents 10, 0, 15 @ N=3 
    #input: list[int]
    #output: string if 0 and 1
    DNA = ''
    for i in indi:
        bi = bin(i)[2:]
        #formate the DNA to be 5 numbers
        if (len(bi) > 5):
            print("error at get DNA")
        while(len(bi)!=5):
            bi = '0'+bi
        
        DNA = DNA + bi
    return DNA

def DNAtoIndi(DNA):
    #convert DNA(string) to decimal representation
    #input string
    #output list[int]
    indi = []
    for i in range(N):
        indi.append(int(DNA[i*5:(i+1)*5],2))
    return indi

