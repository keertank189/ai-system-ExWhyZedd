#EXWHYZED
import os
import sys
import random
#Primary grid to store GamePlay
GRID=[[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ']] 
#-----------------------------------------------------------------------------
#Class to create Player Profile
#-----------------------------------------------------------------------------
class Player:
	'Creates a Player Profile for each player'
	def __init__(self,name,marker):
		self.name=name
		self.marker=marker
MARKERS=['X','Y','Z']
#-----------------------------------------------------------------------------
#GamePlay
#-----------------------------------------------------------------------------
def board():
	#Function to print the Game board and the values stored in the grid.
	print("\n"*8)
	print("\t\t\t\t\t    ","*"*56,sep="")
	print("\t\t\t\t\t    *          |          |          |          |          *")
	print("\t\t\t\t\t    *    ",GRID[0][0],"     |    ",GRID[0][1],"     |    ",GRID[0][2],"     |    ",GRID[0][3],"     |    ",GRID[0][4],"     *", sep='')
	print("\t\t\t\t\t    *         1|         2|         3|         4|         5*")
	print("\t\t\t\t\t    *------------------------------------------------------*")
	print("\t\t\t\t\t    *          |          |          |          |          *")
	print("\t\t\t\t\t    *    ",GRID[1][0],"     |    ",GRID[1][1],"     |    ",GRID[1][2],"     |    ",GRID[1][3],"     |    ",GRID[1][4],"     *", sep='')
	print("\t\t\t\t\t    *         6|         7|         8|         9|        10*")
	print("\t\t\t\t\t    *------------------------------------------------------*")
	print("\t\t\t\t\t    *          |          |          |          |          *")
	print("\t\t\t\t\t    *    ",GRID[2][0],"     |    ",GRID[2][1],"     |    ",GRID[2][2],"     |    ",GRID[2][3],"     |    ",GRID[2][4],"     *", sep='')
	print("\t\t\t\t\t    *        11|        12|        13|        14|        15*")
	print("\t\t\t\t\t    *------------------------------------------------------*")
	print("\t\t\t\t\t    *          |          |          |          |          *")
	print("\t\t\t\t\t    *    ",GRID[3][0],"     |    ",GRID[3][1],"     |    ",GRID[3][2],"     |    ",GRID[3][3],"     |    ",GRID[3][4],"     *", sep='')
	print("\t\t\t\t\t    *        16|        17|        18|        19|        20*")
	print("\t\t\t\t\t    *------------------------------------------------------*")
	print("\t\t\t\t\t    *          |          |          |          |          *")
	print("\t\t\t\t\t    *    ",GRID[4][0],"     |    ",GRID[4][1],"     |    ",GRID[4][2],"     |    ",GRID[4][3],"     |    ",GRID[4][4],"     *", sep='')
	print("\t\t\t\t\t    *        21|        22|        23|        24|        25*")
	print("\t\t\t\t\t    ","*"*56,sep="")
def isMovesLeft(l):
	return any(i==' ' for i in sum(l,[]))
def Allocate(l,dir):
	'''
	Function which recursively 
	checks if a valid win sequence exits
	'''
	n=[0,0]
	if dir==90:                         #North
		n[0],n[1]=l[0]-1,l[1]
	if dir==-90:                        #South
		n[0],n[1]=l[0]+1,l[1]
	if dir==0:                          #East
		n[0],n[1]=l[0],l[1]+1
	if dir==180:                        #West
		n[0],n[1]=l[0],l[1]-1
	if dir==45:                         #North-East
		n[0],n[1]=l[0]-1,l[1]+1
	if dir==-135:                       #South-West
		n[0],n[1]=l[0]+1,l[1]-1
	if dir==135:                        #North-West
		n[0],n[1]=l[0]-1,l[1]-1
	if dir==-45:                        #South-East
		n[0],n[1]=l[0]+1,l[1]+1
	if n[0]==-1:
		n[0]=4
	if n[0]==5:
		n[0]=0
	if n[1]==-1:
		n[1]=4
	if n[1]==5:
		n[1]=0
	if (GRID[l[0]][l[1]]==GRID[n[0]][n[1]]):
		return 1+Allocate(n,dir)
	else:
		return 0
def check_win(l):
	def sum(x,y):
		if x+y>=3:
			return 1
		else:
			return 0
	directions=[[90,-90],[180,0],[45,-135],[-45,135]]
	win=list(map(sum,[Allocate(l,L[0]) for L in directions],[Allocate(l,L[1]) for L in directions]))
	if any(win):
		return 1
	else:
		return 0
def evaluate():
	#return (10,randomComputer())
	temp=[0,0]
	for i in range(1,26):
		temp[0]=int((i-1)/5)
		temp[1]=int((i-1)%5)
		if(GRID[temp[0]][temp[1]]!=' '):
			continue
		GRID[temp[0]][temp[1]]='Z'
		if(check_win(temp)==1):
			GRID[temp[0]][temp[1]]=' '
			return (10,i)
		GRID[temp[0]][temp[1]]=' '
	return (0,0)
def minimax(P,player,depth):
	if(depth==0):
		return evaluate()
	temp=[0,0]
	score=-1
	move=-1
	for i in range(1,26):
		temp[0]=int((i-1)/5)
		temp[1]=int((i-1)%5)
		int((i-1)%5)
		if(GRID[temp[0]][temp[1]]==' '):
			GRID[temp[0]][temp[1]]=P[player].marker
			if(check_win(temp)==1):
				thisScore=(20,i)
			else:
				thisScore=minimax(P,(player+1)%3,depth-1)
			if(thisScore[0]>score):
				score=thisScore[0]
				move=thisScore[1]
			GRID[temp[0]][temp[1]]=' '
	if(move==-1):
		return 0
	return (score,move)
def computer(P):
	t=minimax(P,2,2)
	if(type(t)==int):
		return randomComputer()
	elif(t[0]==0):
		return randomComputer()
	else:
		return t[1]
def randomComputer():
	l=[]
	for i in range(1,26):
		temp1=int((i-1)/5)
		temp2=int((i-1)%5)
		if GRID[temp1][temp2]==' ':
			l.append(i)
	return random.choice(l)
def Play():
	point=-1
	p,play=0,[0,0]
	garbage=os.system("clear")
	P=[Player(input(''.join(["Player "+str(i+1)+": "])),MARKERS[i]) for i in range(3)]
	for i in range(1,26):
		point=point+1 if point<2 else 0
		if(i%3==0):
			p=computer(P)
			#p=randomComputer()
		else:
			garbage=os.system("clear")
			board()
			print("\t\t\t\t\t\t    ",P[point].name,"'s Turn: ",sep='',end='')
			p=input()
		if(p=='q'or p=='Q'):
			exit()
		p=int(p)
		play[0]=int((p-1)/5)
		play[1]=int((p-1)%5)
		if GRID[play[0]][play[1]]==' ':
			GRID[play[0]][play[1]]=P[point].marker
		garbage=os.system("clear")
		board()
		if(check_win(play)):
			garbage=os.system("clear")
			board()
			print("\t\t\t\t\t\t    ",P[point].name," Wins!",sep='')
			exit()
	print("It's a Tie!")
#----------------------------------------------------------------------------------------------------------
#Home Screen
#----------------------------------------------------------------------------------------------------------
def Homescreen():
	garbage=os.system("clear")
	print("\n\n\n\n\n\n")
	print("\t\t\t\t      xxxxx           xxxxx   yyyyy           yyyyy     zzzzzzzzzzzzzzzzzzz ")
	print("\t\t\t\t      xxxxx         xxxxx     yyyyy         yyyyy     zzzzzzzzzzzzzzzzzzz  ")
	print("\t\t\t\t        xxxxx       xxxxx       yyyyy       yyyyy     zzzzzzzzzzzzzzzzzz    ")
	print("\t\t\t\t         xxxxx     xxxxx         yyyyy     yyyyy              zzzzzzz       ")
	print("\t\t\t\t          xxxxx   xxxxx           yyyyy   yyyyy              zzzzzz   z     ")
	print("\t\t\t\t           xxxxx xxxxx             yyyyy yyyyy              zzzzz  zzz      ")
	print("\t\t\t\t           xxxxx xxxxx              yyyy yyyy              zzzz  zzzz       ")
	print("\t\t\t\t          xxxxx   xxxxx             yyyy yyyy             z   zzzzzz        ")
	print("\t\t\t\t         xxxxx     xxxxx            yyyy yyyy              zzzzzzzz         ")
	print("\t\t\t\t        xxxxx       xxxxx           yyyy yyyy            zzzzzzzzzzzzzzzzzz ")
	print("\t\t\t\t       xxxxx         xxxxx          yyyy yyyy          zzzzzzzzzzzzzzzzzzz  ")
	print("\t\t\t\t      xxxxx           xxxxx         yyyy yyyy         zzzzzzzzzzzzzzzzzzz   ")
	print()
	print()
	print("\t\t\t\t     *********************************************************************")
	print("\t\t\t\t     * Press:                          | Developed by:                   *")
	print("\t\t\t\t     *        Enter to Start           |      Keertan, Kaushik and Kevin *")
	print("\t\t\t\t     *        Q to quit                |      CSE-C                      *")
	print("\t\t\t\t     *                                 |      PES University             *")
	print("\t\t\t\t     *********************************************************************")
	return sys.stdin.read(1)
'''
-------------------------------------------------------------------------------------------------------------
Game starts here
-------------------------------------------------------------------------------------------------------------
'''
if __name__=='__main__':
	while(1):
		garbage=os.system("clear")
		choice=Homescreen()
		if choice=='\n':
			Play()
		elif choice=='Q' or choice=='q':
			garbage=os.system("clear")
			exit()
		else:
			pass
'''
--------------------------------------------------------------------------------------------------------------
'''
