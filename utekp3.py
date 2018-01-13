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


def block_step(key, message, op):
    #encypting or dectyptin message using block step  encryptation
    #key: a list of key
    #message: a string of message
    #op = 1 : enctypt;  op = 0 : decrypt
    
    '''print ( block_step([1, 3, 5], 'ALPHABETIZE! THIS!', 1))
    >>>BOUIDGFWNAH! YILX!
    '''
    if (op == 0):
        for i in range(len(key)):#convert key to negative
            key[i] = -key[i]      
            
    r = []
    count = 0 #this counts how many words has been en/decy
    for j in range(len(message)):
        i = message[j]
        if (ord(i)<=90 and ord(i) >=65):
            pkey = count%len(key)#position of key
            newp = (ord(i)-65+key[pkey])%26+65
            newi = chr(newp)
            r.append(newi) 
            count += 1
        else:
            r.append(i)
            
        return ''.join(r)



def StepCode2A(inputString):
    #3A
    ScoreList = [];
    
    for i in range(26):
        #DeString is the string decrypted
        DeString = EDncrypt(i, inputString, 0);
        #ScoreList.append(Evaluate(DeString));
        ScoreList.append(1);
    
    Max = max(ScoreList);
    
    print ScoreList.index(Max);
    print Max;
    

def StepCode2B(inputString, keyLen):



    
StepCode2A("afsadfadwsdc")


 
 
 
