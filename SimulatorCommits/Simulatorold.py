import sys

R=['000','001','010','011','100','101','110']

lst=[]
for v in sys.stdin:         #Taking Input from file
    lst.append(v)

def BtoD(a):
    d=0
    for i in range(len(a)):
        d=d+(2**i)*int(a[len(a)-1-i])
    return d

def Dtob(n):                # Converting integer to 8-bit binary number
    a=bin(n).replace("0b", "")      # Developer:-SIDDHANT
    while(len(a)!=8):
        a='0'+a
    return a

def Dtob2(n):               # Converting integer to 16-bit binary number
    a=bin(n).replace("0b", "")      # Developer:-SIDDHANT
    while(len(a)!=16):
        a='0'+a
    return a

REG=[0,0,0,0,0,0,0]
FLAGS=0
V=0
L=0
G=0
E=0

pc=0

while(pc<len(lst)):

    lst[pc]=lst[pc].rstrip()

    if(lst[pc][0:5]=='00000'):                                                            #add
        REG[BtoD(lst[pc][7:10])] = REG[BtoD(lst[pc][10:13])] + REG[BtoD(lst[pc][13:16])]
        if(REG[BtoD(lst[pc][7:10])] > 255):
            V=1
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))
    
    if(lst[pc][0:5]=='00001'):                                                            #sub
        REG[BtoD(lst[pc][7:10])] = REG[BtoD(lst[pc][10:13])] - REG[BtoD(lst[pc][13:16])]
        if(REG[BtoD(lst[pc][7:10])] < 0):
            V=1
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))

    if(lst[pc][0:5]=='00110'):                                                            #mul
        REG[BtoD(lst[pc][7:10])] = REG[BtoD(lst[pc][10:13])] * REG[BtoD(lst[pc][13:16])]
        if(REG[BtoD(lst[pc][7:10])] > 255 ):
            V=1
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))
    
    if(lst[pc][0:5]=='01010'):                                                            #xor
        REG[BtoD(lst[pc][7:10])] = REG[BtoD(lst[pc][10:13])] ^ REG[BtoD(lst[pc][13:16])]
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))
    
    if(lst[pc][0:5]=='01011'):                                                            #or
        REG[BtoD(lst[pc][7:10])] = REG[BtoD(lst[pc][10:13])] | REG[BtoD(lst[pc][13:16])]
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))
    
    if(lst[pc][0:5]=='01100'):                                                            #and
        REG[BtoD(lst[pc][7:10])] = REG[BtoD(lst[pc][10:13])] & REG[BtoD(lst[pc][13:16])]
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))

    
    if(lst[pc][0:5:1]=='00100'):                                                #ld
        
        REG[BtoD(lst[pc][5:8:1])] = BtoD((lst[pc][8:16:1]))
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))


    if(lst[pc][0:5:1]=='00101'):                                                #st
        if(lst[pc][5:8:1] in R ):
            
            print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))


    if(lst[pc][0:5:1]=='00010'):                                                #mov imm
        REG[BtoD(lst[pc][5:8:1])] = BtoD(lst[pc][8:16])
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))


    if(lst[pc][0:5:1]=='01000'):                                                #rs
        REG[BtoD(lst[pc][5:8])]=REG[BtoD(lst[pc][5:8])] >> BtoD(lst[pc][8:16])
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))


    if(lst[pc][0:5:1]=='01001'):                                                #ls
        REG[BtoD(lst[pc][5:8])]=REG[BtoD(lst[pc][5:8])] << BtoD(lst[pc][8:16])
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))    

    if(lst[pc][0:5:1]=='00011'):                                                #mov reg
        REG[BtoD(lst[pc][10:13])]=REG[BtoD(lst[pc][13:16])]
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))

    if(lst[pc][0:5:1]=='00111'):                                                #div
        REG[0] = REG[BtoD(lst[pc][10:13])] / REG[BtoD(lst[pc][13:16])]
        REG[1] = REG[BtoD(lst[pc][10:13])] % REG[BtoD(lst[pc][13:16])]
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))
    
    if(lst[pc][0:5:1]=='01101'):                                                #not
        REG[BtoD(lst[pc][10:13])] = ~(REG(BtoD(lst[pc][13:16])))
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))
    
    if(lst[pc][0:5:1]=='01110'):                                                #cmp
        r1 = REG[BtoD(lst[pc][10:13])] 
        r2 = REG[BtoD(lst[pc][13:16])]
        if(r1 > r2):
            G=1
        elif(r1 < r2):
            L=1
        else:
            E=1
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))


    if(lst[pc][0:5]=='10011' and lst[pc][5:16]=='00000000000'):             #hlt
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))

    pc+=1


for i in lst:
    print(i)


t=len(lst)

while(t<256):
    print('0000000000000000')
    t=t+1