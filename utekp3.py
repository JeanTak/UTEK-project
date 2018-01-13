import math

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
    
def count(s):
    f = open('trainningset.txt','r')
    txt = f.read()
    dataset = txt
    #dataset = ' A quick fox jumps over a lazy bear'
    dataset = dataset.replace("N", "")
    dataset = dataset.replace("<unk>","")
    dataset = dataset.upper()
    
    pos = 0;
    c = 0;

    while (dataset.find(s, pos) != -1):
        pos = dataset.find(s,pos) + 1
        c = c + 1
    return c        

def Pr(s):
    if (len(s) == 1):
        if (count(s) != 0):
            return 1 * 10
        else:
            return 0
    Sum = 0;
    ru = 10;
    for i in range(len(s)):
        i += 1
        ru = ru * 10
        d = float(count(s[:(i - 1)]))
        if (d != 0):
            Sum = Sum + ru * count(s[:i]) / d
    return Sum

def Evaluate(target):
    target = target.split(' ')
    Sum = 0;
    for i in range(len(target)):
        pr = Pr(target[i])
        if (pr != 0):
            Sum = Sum + math.log(pr,10)
    return Sum 

#main






def StepCode3A(inputString):
    #3A
    ScoreList = [];
    
    for i in range(26):
        #DeString is the string decrypted
        DeString = EDncrypt(i, inputString, 0);
        ScoreList.append(Evaluate(DeString));
    
    Max = max(ScoreList);
    
    print ScoreList.index(Max);
    print Max;
    

f = open('trainningset.txt','r')
txt = f.read()
dataset = txt
#dataset = 'A quick fox jumps over a lazy bear'
dataset = dataset.replace("N", "")
dataset = dataset.replace("<unk>","")
dataset = dataset.upper()
dataset = dataset.split(' ')

database = []
for i in range(len(dataset)):
    if (len(dataset[i]) <= 7):
        database.append(dataset[i])
        
database = list(set(database))

#test purpose
#for i in range(len(database)):
    #database[i] = database[i].replace(database[i], database[i] + str(count(database[i])))

dataset = ' '.join(dataset)
#print(dataset)
#print(database)    
Input = input()
StepCode2A(Input)


 
 
 
