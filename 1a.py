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
f = open('../input/1a.in','r')
outf = open('../output/1a.out','w')
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
        outf.write(EDncrypt(int(command[1]),command[2],op)+'\n')

f.close()
outf.close()



        
    