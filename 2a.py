'''
Input: ENCRYPT|1 3 5|ALPHABETIZE! THIS!
Output: BOUIDGFWNAH! YILX!
'''

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

#inpout and output part
f = open('../input/1b.in','r')
outf = open('../output/1b.out','w')
fstr = f.read()
#read input file and output to output file
commandlist = fstr.split('\n')
for command in commandlist:
    command = command.split(' | ')
    if (command[0] == 'ENCRYPT'):
        op=1
    else:
        op =0
    key = command[1].split(" ")
    
    for i in range(len(key)):#convert key from str to int
        key[i] = int(key[i])
    message = command[2]
    outf.write(block_step(key,message,op)+'\n')

f.close()
outf.close()



                  