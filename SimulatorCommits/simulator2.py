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

def Dtob2(n):               # Converting integer to 8-bit binary number
    a=bin(n).replace("0b", "")      # Developer:-SIDDHANT
    while(len(a)!=16):
        a='0'+a
    return a

REG=[0,0,0,0,0,0,0]
FLAGS=0



pc=0
i=0
while(pc<(len(lst)-i)):

    lst[pc]=lst[pc].rstrip()

    if(lst[pc][0:5:1]=='00000'):
        REG[BtoD(lst[pc][7:10])]=REG[BtoD(lst[pc][10:13])] + REG[BtoD(lst[pc][13:16])]
        if(REG[BtoD(lst[pc][7:10])] > 255):
            V=1
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))

    
    if(lst[pc][0:5:1]=='00001'):
        REG[BtoD(lst[pc][7:10])]=REG[BtoD(lst[pc][10:13])] - REG[BtoD(lst[pc][13:16])]
        if(REG[BtoD(lst[pc][7:10])] < 0):
            V=1
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))
    


    if(lst[pc][0:5:1]=='00101'):
        if(lst[pc][5:8:1] in R ):
            lst.append(Dtob2(REG[BtoD(lst[pc][5:8:1])]))
            i=i+1
            print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))


    if(lst[pc][0:5:1]=='00100'):
        if(lst[pc][5:8:1] in R ):
            REG[BtoD(lst[pc][5:8:1])]=BtoD(lst[pc][5:8:1])
            print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))



    if(lst[pc][0:5:1]=='00010'):
        if(lst[pc][5:8:1] in R ):
            if(0<=BtoD(lst[pc][8:16:1])<256):
                REG[BtoD(lst[pc][5:8:1])]=BtoD((lst[pc][8:16:1]))
                print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))


    if(lst[pc][0:5:1]=='01000'):
        if(lst[pc][5:8:1] in R ):
            if(0<=BtoD(lst[pc][8:16:1])<256):
                REG[BtoD(lst[pc][5:8:1])]=REG[BtoD(lst[pc][5:8:1])]>>BtoD((lst[pc][8:16:1]))
                print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))


    if(lst[pc][0:5:1]=='01001'):
        if(lst[pc][5:8:1] in R ):
            if(0<=BtoD(lst[pc][8:16:1])<256):
                REG[BtoD(lst[pc][5:8:1])]=REG[BtoD(lst[pc][5:8:1])]<<BtoD((lst[pc][8:16:1]))
                print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))          




    if(lst[pc][0:5:1]=='10011' and lst[pc][5:16:1]=='00000000000'):
        print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))


    pc=pc+1


for i in lst:
    print(i)


t=len(lst)

while(t<256):
    print('0000000000000000')
    t=t+1
