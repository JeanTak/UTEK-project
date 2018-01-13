import math

TRANNINGSET = 10000000

def EDncrypt(k,rawin,op):
    #NOTE THAT op=1 -> Encrypt op=0->decrypton
    #chr(65) = 'A'
    #chr(90) = 'Z'
    '''EDncrypt(25,'REMEMBER TO WRAP PROPERLY',1)
    >>>QDLDLADQ SN VQZO OQNODQKX
    '''
    
    if(op==0):
        k = -k
    r = []
    for i in rawin:
        if (ord(i)<=90 and ord(i) >=65):
            newp = (ord(i)-65+k)%26+65
            newi = chr(newp)
            r.append(newi) 
        else:
            r.append(i)
        
    return ''.join(r)       

def Pr(s,database):
    if (len(s) == 1):
        if (database.count(s) != 0):
            return 1 * 10
        else:
            return 0
    Sum = 0;
    ru = 10;
    for i in range(len(s)):
        i += 1
        ru = ru * 10
        d = float(database.count(s[:(i - 1)]))
        if (d != 0):
            Sum = Sum + ru * database.count(s[:i]) / d
    return Sum

def Evaluate(target,database):
    target = target.split(' ')
    Sum = 0;
    for i in range(len(target)):
        pr = Pr(target[i],database)
        if (pr != 0):
            Sum = Sum + math.log(pr,10)
    return Sum 

def StepCode3A(inputString,database):
    #3A
    ScoreList = [];
    
    for i in range(26):
        #DeString is the string decrypted
        DeString = EDncrypt(i, inputString, 0);
        S = Evaluate(DeString,database)
        ScoreList.append(S);
        print ("when k = ",i,EDncrypt(i, inputString, 0),"score = ", S)
    
    Max = max(ScoreList);
    k=ScoreList.index(Max)
    
    print ("k is ", k);
    print Max;
    print ("the sentence is "+EDncrypt(k, inputString, 0))
    

'''f = open('trainningset.txt','r')
txt = f.read()
dataset = txt[:TRANNINGSET]
dataset = dataset.replace("N", "")
dataset = dataset.replace("<unk>","")
dataset = dataset.upper()
dataset = dataset.split(' ')
     
#database = list(set(database))

#test purpose
#for i in range(len(database)):
    #database[i] = database[i].replace(database[i], database[i] + str(count(database[i])))


#print(dataset)
#print(database)  '''

f = open('trainningset.txt','r')
txt = f.read()
dataset = txt[:TRANNINGSET]
dataset = dataset.replace("N", "")
dataset = dataset.replace("<unk>","")
dataset = dataset.upper()
database = dataset

'''database = []
for i in range(len(dataset)):
    if (len(dataset[i]) <= 7):
        database.append(dataset[i])
database = ' '.join(database)'''



Input = 'RQIVGIVO EC, EPW QA PM? Q LWVB SVWE???'
StepCode3A(Input, database)




 
 
 
