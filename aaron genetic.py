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

def select_Pair(prob_of_sur, generation):
    #prob_of_sur ->[0.234, 0.6543 ...]
    #generation ->[[1,2,3], [4,2,7]...]
    Sum = float(sum(prob_of_sur))
    factor = 1 / Sum
    #these two steps is to make teh sum of probability is 1
    
    for i in range(POPULATION):
        #here is to
        if(i == 0):
            prob_of_sur[i] = prob_of_sur[i] * factor;
        else:
            prob_of_sur[i] = prob_of_sur[i] * factor + prob_of_sur[i-1];
    
    MomPercent = random.uniform(0, 1)
    DadPercent = random.uniform(0, 1)
    ParentList=[];
    
    for i in range(POPULATION):
        if(i==0):
            if(MomPercent<prob_of_sur[i]):
                ParentList.append(generation[i]);
                break;                
        
        else:
            if(MomPercent<prob_of_sur[i] and MomPercent>prob_of_sur[i-1]):
                ParentList.append(generation[i]);
                break;
            
    for i in range(POPULATION):
        if(i==0):
            if(DadPercent<prob_of_sur[i]):
                ParentList.append(generation[i]);
                break;                
                
        else:
            if(DadPercent<prob_of_sur[i] and DadPercent>prob_of_sur[i-1]):
                ParentList.append(generation[i]);
                break;
    
    '''for i in range(POPULATION):
        if(DadPercent<prob_of_sur[i] and DadPercent>prob_of_sur[i-1]):
            if(generation[i] == ParentList[0]):
                DadPercent = random.uniform(0, 1)
                i = 0;
            else:
                ParentList.append(generation[i]);
 '''           
    return ParentList

