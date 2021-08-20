import sys
R=['000','001','010','011','100','101','110']
FLAGS='111'
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

f1=0
f2=0
lst=[]
z=''
lst1=[]

for v in sys.stdin:         #Taking Input from file
	lst.append(v)           #Developer:-Jaskaran
	lst1.append(v)
label={}
dic={}
i=0
x=0

while(i<len(lst)):                                  # Handling Variables and labels.
	if(lst[i][0:3:1]=='var'):                       #Developer:- SIDDHANT
		dic.update({lst[i][4:len(lst[i])-1:1]:0})
		lst.remove(lst[i])
		i-=1
	if(i>=0):
		for j in range(len(lst[i])):
			if(lst[i][j]==':'):
				x=j
				label.update({lst[i][0:x:1]:i})
				lst[i]=lst[i][x+2:len(lst[i]):1]
				break
	if(lst[i][0:3]=='hlt'):
		f2+=1
	i=i+1

y=0
for i in dic:                   #storing the value of variable
	dic[i]=len(lst)+y           #Developer:-SIDDHANT
	y=y+1


pc=0
REG=[0,0,0,0,0,0,0]
FLAGS=0


while(pc<len(lst)):
	lst[pc]=lst[pc].rstrip()
	word=lst[pc].split()
	if(word[0]=='add'):
		x=int(word[1][1])
		y=int(word[2][1])
		z=int(word[3][1])
		REG[x]=REG[y] + REG[z]
		if(REG[x]>255):
			V=1
		print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))


	if(lst[pc][0:3]=='mov'):                                                       
		if(lst[pc][4]=='R' and ((0<=int(lst[pc][5])<=6) and lst[pc][6]==" ")):
			if( lst[pc][7]=='$'):                                                  
				if(0<=int(lst[pc][8:len(lst[pc]):1])<=255):
					REG[int(lst[pc][5])]=int(lst[pc][8:len(lst[pc]):1])
					print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))

	if(lst[pc][0:3]=='mov'):                       
		if(lst[pc][4]=='R'):                       
			if(0<=int(lst[pc][5])<7):
				if(lst[pc][7]=='R'):
					if(0<=int(lst[pc][8])<7):
						REG[int(lst[pc][5])]=REG[int(lst[pc][8])]
						print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))

	if(lst[pc][0:3]=='hlt'):
		print(Dtob(pc)+' '+ Dtob2(REG[0])+' '+ Dtob2(REG[1])+' '+ Dtob2(REG[2])+' '+ Dtob2(REG[3])+' '+ Dtob2(REG[4])+' '+ Dtob2(REG[5])+' '+ Dtob2(REG[6])+' '+ Dtob2(FLAGS))
	pc=pc+1


ind=0
while(ind<len(lst)):
	lst[ind]=lst[ind].rstrip()
	z=''
	if(f1==1):                                                      #Instruction after halt error handling
		print('Line '+ str(ind+1) +' Error: Instruction after halt')#Developer:- Jaskaran
		break
	word = lst[ind].split()
	f3=0
	f4=0

	if(word[0]=='add'):                         #Handling Type A Instructions
		if(lst[ind][4]=='R' and int(word[1][-1:])<7 and lst[ind][7]=='R' and int(word[2][-1:])<7 and lst[ind][10]=='R' and int(word[3][-1:])<7):
			x=word[1][-1:]                      # Developer:-JASKARAN
			i2=str(R[int(x)])
			y=word[2][-1:]
			i3=str(R[int(y)])
			z=word[3][-1:]
			i4=str(R[int(z)])
			print('0000000'+i2+i3+i4)
		elif(lst[ind][4:9:1]=='FLAGS' or lst[ind][7:12:1]=='FLAGS' or lst[ind][10:15:1]=='FLAGS'):
			print('Line '+ str(ind+1)+" Error: Illegal use of FLAGS register")  
		else:
			print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
			break

	if(word[0]=='sub'):
		if(lst[ind][4]=='R' and int(word[1][-1:])<7 and lst[ind][7]=='R' and int(word[2][-1:])<7 and lst[ind][10]=='R' and int(word[3][-1:])<7):
			x=word[1][-1:]
			i2=str(R[int(x)])
			y=word[2][-1:]
			i3=str(R[int(y)])
			z=word[3][-1:]
			i4=str(R[int(z)])
			print('0000100'+i2+i3+i4)
		elif(lst[ind][4:9:1]=='FLAGS' or lst[ind][7:12:1]=='FLAGS' or lst[ind][10:15:1]=='FLAGS'):
			print('Line '+ str(ind+1)+" Error: Illegal use of FLAGS register")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
			break

	if(word[0]=='mul'):
		if(lst[ind][4]=='R' and int(word[1][-1:])<7 and lst[ind][7]=='R' and int(word[2][-1:])<7 and lst[ind][10]=='R' and int(word[3][-1:])<7):
			x=word[1][-1:]
			i2=str(R[int(x)])
			y=word[2][-1:]
			i3=str(R[int(y)])
			z=word[3][-1:]
			i4=str(R[int(z)])
			print('0011000'+i2+i3+i4)
		elif(lst[ind][4:9:1]=='FLAGS' or lst[ind][7:12:1]=='FLAGS' or lst[ind][10:15:1]=='FLAGS'):
			print('Line '+ str(ind+1)+" Error: Illegal use of FLAGS register")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
			break

	if(word[0]=='xor'):
		if(lst[ind][4]=='R' and int(word[1][-1:])<7 and lst[ind][7]=='R' and int(word[2][-1:])<7 and lst[ind][10]=='R' and int(word[3][-1:])<7):
			x=word[1][-1:]
			i2=str(R[int(x)])
			y=word[2][-1:]
			i3=str(R[int(y)])
			z=word[3][-1:]
			i4=str(R[int(z)])
			print('0101000'+i2+i3+i4)
		elif(lst[ind][4:9:1]=='FLAGS' or lst[ind][7:12:1]=='FLAGS' or lst[ind][10:15:1]=='FLAGS'):
			print('Line '+ str(ind+1)+" Error: Illegal use of FLAGS register")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
			break

	if(word[0]=='or'):
		if(lst[ind][4]=='R' and int(word[1][-1:])<7 and lst[ind][7]=='R' and int(word[2][-1:])<7 and lst[ind][10]=='R' and int(word[3][-1:])<7):
			x=word[1][-1:]
			i2=str(R[int(x)])
			y=word[2][-1:]
			i3=str(R[int(y)])
			z=word[3][-1:]
			i4=str(R[int(z)])
			print('0101100'+i2+i3+i4)
		elif(lst[ind][4:9:1]=='FLAGS' or lst[ind][7:12:1]=='FLAGS' or lst[ind][10:15:1]=='FLAGS'):
			print('Line '+ str(ind+1)+" Error: Illegal use of FLAGS register")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
			break

	if(word[0]=='and'):
		if(lst[ind][4]=='R' and int(word[1][-1:])<7 and lst[ind][7]=='R' and int(word[2][-1:])<7 and lst[ind][10]=='R' and int(word[3][-1:])<7):
			x=word[1][-1:]
			i2=str(R[int(x)])
			y=word[2][-1:]
			i3=str(R[int(y)])
			z=word[3][-1:]
			i4=str(R[int(z)])
			print('0110000'+i2+i3+i4)
		elif(lst[ind][4:9:1]=='FLAGS' or lst[ind][7:12:1]=='FLAGS' or lst[ind][10:15:1]=='FLAGS'):
			print('Line '+ str(ind+1)+" Error: Illegal use of FLAGS register")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
			break

	if(word[0]=='ld'):                               #Handling Type D Instructions  
		if(lst[ind][3]=='R' and int(word[1][-1:])<7):#Developer:-JASKARAN
			x=word[1][-1:]
			i2=str(R[int(x)])
			y=word[2]
			for i in dic:
				if y==i:
					z=Dtob(dic[i])
					f3=1
			if(f3==0):
				print('Line '+ str(ind+1)+" Error: Invalid variable")
				break
			while(len(z)!=8):
				z='0'+z
			print('00100'+i2+z)
		elif(lst[ind][3:8:1]=='FLAGS'):
			print('Line '+ str(ind+1)+" Error: Illegal use of FLAGS register")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
			break

	if(word[0]=='st'):              
		if(lst[ind][3]=='R' and int(word[1][-1:])<7):
			x=word[1][-1:]
			i2=str(R[int(x)])
			y=lst[ind][6:len(lst[ind]):1]
			for i in dic:
				if y==i:
					z=Dtob(dic[i])
					f4=1
			if(f4==0):
				print('Line '+ str(ind+1)+" Error: Invalid variable")
				break
			while(len(z)!=8):
				z='0'+z
			print('00101'+i2+z)
		elif(lst[ind][3:8:1]=='FLAGS'):
			print('Line '+ str(ind+1)+" Error: Illegal use of FLAGS register")
		else:
			print('Line '+ str(ind+1)+' Error: Invalid syntax or register')
			break


	
	if(lst[ind][0:3]=='mov'):                                                       #Handling Type B Instructions
		if(lst[ind][4]=='R' and ((0<=int(lst[ind][5])<=6) and lst[ind][6]==" ")):
			if( lst[ind][7]=='$'):                                                  #Developer:-SIDDHANT
				if(0<=int(lst[ind][8:len(lst[ind]):1])<=255):
					print('00010'+R[int(lst[ind][5])]+Dtob(int(lst[ind][8:len(lst[ind]):1])))
				else:
					print('Line '+ str(ind+1)+" Error: Invalid immediate value")
					break
		elif(lst[ind][4:9:1]=='FLAGS'):
			print('Line '+ str(ind+1)+" Error: Illegal use of FLAGS register")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
			break

	if(lst[ind][0:2]=='ls'):
		if(lst[ind][3]=='R' and ((0<=int(lst[ind][4])<=6) and lst[ind][5]==" ")):
			if( lst[ind][6]=='$'):
				if(0<=int(lst[ind][7:len(lst[ind]):1])<=255):
					print('01001'+R[int(lst[ind][4])]+Dtob(int(lst[ind][7:len(lst[ind]):1])))
				else:
					print('Line '+ str(ind+1)+" Error: Invalid immediate value")
					break
		elif(lst[ind][3:8:1]=='FLAGS'):
			print('Line '+ str(ind+1)+" Error: Illegal use of FLAGS register")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
			break   

	if(lst[ind][0:2]=='rs'):
		if(lst[ind][3]=='R' and ((0<=int(lst[ind][4])<=6) and lst[ind][5]==" ")):
			if( lst[ind][6]=='$'):
				if(0<=int(lst[ind][7:len(lst[ind]):1])<=255):
					print('01000'+R[int(lst[ind][4])]+Dtob(int(lst[ind][7:len(lst[ind]):1])))
				else:
					print('Line '+ str(ind+1)+" Error: Invalid immediate value")
					break
		elif(lst[ind][3:8:1]=='FLAGS'):
			print('Line '+ str(ind+1)+" Error: Illegal use of FLAGS register")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
			break

	if(lst[ind][0:3]=='mov'):                       #Handling Type C Instructions
		if(lst[ind][4]=='R'):                       #Developer:-Rahul
			if(0<=int(lst[ind][5])<7):
				if(lst[ind][7]=='R'):
					if(0<=int(lst[ind][8])<7):
						print('00011'+'00000'+R[int(lst[ind][5])]+R[int(lst[ind][8])])
				if(lst[ind][7:12:1]=='FLAGS'):
					print('0001100000'+R[int(lst[ind][5])]+FLAGS)
		elif(lst[ind][4:9:1]=='FLAGS' or lst[ind][7:12:1]=='FLAGS'):
			print('Line '+ str(ind+1)+" Error: Illegal use of FLAGS register")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
			break

	if(lst[ind][0:3]=='div'):
		if(lst[ind][4]=='R'):
			if(0<=int(lst[ind][5])<7):
				if(lst[ind][7]=='R'):
					if(0<=int(lst[ind][8])<7):
						print('0011100000'+R[int(lst[ind][5])]+R[int(lst[ind][8])])
				else:
					print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
					break
		elif(lst[ind][4:9:1]=='FLAGS' or lst[ind][7:12:1]=='FLAGS'):
			print('Line '+ str(ind+1)+" Error: Illegal use of FLAGS register")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
			break

	if(lst[ind][0:3]=='not'):
		if(lst[ind][4]=='R'):
			if(0<=int(lst[ind][5])<7):
				if(lst[ind][7]=='R'):
					if(0<=int(lst[ind][8])<7):
						print('0110100000'+R[int(lst[ind][5])]+R[int(lst[ind][8])])
				else:
					print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
					break
		elif(lst[ind][4:9:1]=='FLAGS' or lst[ind][7:12:1]=='FLAGS'):
			print('Line '+ str(ind+1)+" Error: Illegal use of FLAGS register")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
			break

	if(lst[ind][0:3]=='cmp'):                               #Handling Type E Instructions                   
		if(lst[ind][4]=='R'):                               #Developer:-Rahul
			if(0<=int(lst[ind][5])<7):
				if(lst[ind][7]=='R'):
					if(0<=int(lst[ind][8])<7):      
						print('0111000000'+R[int(lst[ind][5])]+R[int(lst[ind][8])])
				else:
					print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
					break
		elif(lst[ind][4:9:1]=='FLAGS' or lst[ind][7:12:1]=='FLAGS'):
			print('Line '+ str(ind+1)+" Error: Illegal use of FLAGS register")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid syntax or register")
			break

	if(lst[ind][0:3]=='jmp'):                       
		y=lst[ind][4:len(lst[ind]):1]
		if(y in label.keys()):
			for i in dic:
				if y==i:
					z=Dtob(dic[i])
			if(z==''):
				z=Dtob(label[y])
			while(len(z)!=8):
				z='0'+z
		elif(y in dic.keys()):
			print('Line '+ str(ind+1)+" Error: Misuse of variable and label")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid variable or label")
			break
		print('01111000'+z) 

	if(lst[ind][0:3]=='jlt'):
		y=lst[ind][4:len(lst[ind]):1]
		if(y in label.keys()):
			for i in dic:
				if y==i:
					z=Dtob(dic[i])
			if(z==''):
				z=Dtob(label[y])
			while(len(z)!=8):
				z='0'+z
		elif(y in dic.keys()):
			print('Line '+ str(ind+1)+" Error: Misuse of variable and label")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid variable or label")
			break
		print('10000000'+z)

	if(lst[ind][0:3]=='jgt'):
		y=lst[ind][4:len(lst[ind]):1]
		if(y in label.keys()):
			for i in dic:
				if y==i:
					z=Dtob(dic[i])
			if(z==''):
				z=Dtob(label[y])
			while(len(z)!=8):
				z='0'+z
		elif(y in dic.keys()):
			print('Line '+ str(ind+1)+" Error: Misuse of variable and label")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid variable or label")
			break
		print('10001000'+z)

	if(lst[ind][0:2]=='je'):
		y=lst[ind][4:len(lst[ind]):1]
		if(y in label.keys()):
			for i in dic:
				if y==i:
					z=Dtob(dic[i])
			if(z==''):
				z=Dtob(label[y])
			while(len(z)!=8):
				z='0'+z
		elif(y in dic.keys()):
			print('Line '+ str(ind+1)+" Error: Misuse of variable and label")
		else:
			print('Line '+ str(ind+1)+" Error: Invalid variable or label")
			break
		print('10010000'+z)

	if(lst[ind][0:3]=='hlt'):
		if(len(word)>1):
			print('Line '+ str(ind+1) +' Error: Incorrect use of syntax')
			break
		f1+=1
		print('1001100000000000')
	ind=ind+1
if(f2==0):
	print('Error: Missing halt instruction')

k=0
for i in range(len(lst1)):                          #Handling variable instruction after halt
	lst1[i]=lst1[i].rstrip()                        
	if(k>0 and lst1[i][0:3:1]=='var'):
		print('Line '+ str(k+1) + ' Error: Instruction after halt')
	if(lst1[i]=='hlt'):
		k=i+1

t=len(lst)

while(t<256):
	print('0000000000000000')
	t=t+1



# Debugging and Running assembler for Hard and simple test cases:-SIDDHANT
# Making Error statement:-Jaskaran, Rahul and Siddhant
# Debugging Error Cases:- Jaskaran and Rahul