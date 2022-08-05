import random
board=[1,2,3,4,5,6,7,8,9]
gme=True

def display_board(board):
    k=0    
    for j in range(13):
        
        if j%4==0:
            for i in range(25):
                if i%8==0:
                    print("+",end="")
                else:
                    print("-",end="")
            
        else:
            for i in range(25):
                if i%8==0:
                    print("|",end="")
                elif((j==2   or j==6 or j==10) and (i==4 or i==12 or i==20)):
                    print(board[k],end="")
                    k=k+1
                    
                else:
                    print(" ",end="")
        print()
    
def enter_move(board):
    x=int(input("enter your move"))
    if(x>0 and x<10 and board[x-1]==x):
        board[x-1]="O"
    else:
        print("oops wrong choice /nenter again")

def computer_move(board):
    #print("computer move")
    n=random.randrange(0,9)
    if(n>0 and n<10 and board[n-1]==n):
        print("computer move")
        board[n-1]="X"
    else:
        computer_move(board)

def victory_for(board, sign):
    global gme
    if((board[0]==board[1]==board[2]==sign) or (board[3]==board[5]==board[4]==sign) or (board[6]==board[7]==board[8]==sign)):
        print(sign ,"Wins!!")
        gme=False
    elif((board[0]==board[3]==board[6]==sign) or (board[1]==board[4]==board[7]==sign) or (board[2]==board[5]==board[8]==sign)):
        
        print(sign ,"Wins!!")
        gme=False
    elif((board[0]==board[4]==board[8]==sign) or (board[2]==board[4]==board[6]==sign)):
        print(sign ,"Wins!!")
        gme=False
    else:
        gme=True


display_board(board)
while gme:
    
    enter_move(board)
    display_board(board)
    victory_for(board,"O")
    if not gme:
        break;
        
    #print("computer move")
    computer_move(board)
    display_board(board)
    victory_for(board,"X")
    if not gme:
        break;    


    

