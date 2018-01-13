def permu_code(key, rawin, op):
    #key: list of the permutation keys
    #message: string of the input
    #op = 1: enctypt; op = 0: decrypt
    
    '''
    permu_code(['L', 'V', 'T', 'U', 'O', 'E', 'P', 'W', 'Q', 'F', 'N', 'J', 'M', 'K', 'G', 'B', 'R', 'Z', 'I', 'D', 'S', 'A', 'X', 'H', 'Y', 'C'],'THIS SENTENCE IS A FAIRLY TYPICAL ONE AND SHOULD BE EASY TO DECRYPT.',1)
    >>>DWQI IOKDOKTO QI L ELQZJY DYBQTLJ GKO LKU IWGSJU VO OLIY DG UOTZYBD.
    '''
    
    r = []
    for i in rawin:
        if (ord(i)<=90 and ord(i) >=65):
            if (op ==1) :
                p = ord(i)-65
                newi = key[p]
                r.append(newi) 
            else:
                p = key.index(i)
                newi = chr(p+65)
                r.append(newi)    
        else:
            r.append(i)        
            
    return ''.join(r)


#--------------------------------input and ouput part--------------------------------------
f = open('../input/1c.in','r')
outf = open('../output/1c.out','w')
fstr = f.read()
#read input file and output to output file
commandlist = fstr.split('\n')
for command in commandlist:
    if command.strip():
        command = command.split(' | ')
        if (command[0] == 'ENCRYPT'):
            op=1
        else:
            op =0
        
        key = list(command[1])
        message=command[2]
        outf.write(permu_code(key,message,op)+'\n')

f.close()
outf.close()