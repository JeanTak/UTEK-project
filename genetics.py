import random 

POPULATION = 3;

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

print select_Pair([0.8566, 0.2213124, 0.952432],[[1,2],[10,15], [3,4]])