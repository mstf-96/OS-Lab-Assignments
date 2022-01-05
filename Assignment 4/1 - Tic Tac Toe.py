import random
from termcolor import colored, cprint
from colorama import Fore
from os import system, name
from time import time

def clear():
      if name == 'nt':
        _ = system('cls')
      else:
        _ = system('clear')

def print_board(board):
    print('\nBoard :')
    for i in range(3):
        for j in range(3):
            if board[i][j]=='X':
                cprint('X','red',end=' ')
            elif board[i][j]=='O':
                cprint('O','blue',end=' ')
            else:
                print('-',end=' ')
        print()
    print('____________________________________')
'''
def print_board(board):
    print('\nBoard :')
    for i in range(3):
        for j in range(3):
            if board[i][j]=='X':
                    print(Fore.RED + 'X', end=' ')
                    print(Fore.WHITE, end='')
            elif board[i][j]=='O':
                print(Fore.BLUE + 'O', end=' ')
                print(Fore.WHITE, end='')
            else:
                print('-', end=' ')
        print()
    print('____________________________________')
'''
def check_range(board,row,col):
    if 0<=row<=2 and 0<=col<=2:
        if board[row][col]=='-':
            return True
        else:
            print('This cell is not empty , please try again')
            return False
    else:
        print("[ERROR] : row and col must be between 0 and 2")
        return False

def check_result(board,player_symbole):
    w=player_symbole*3
    win=False
    #checking rows
    for i in range(3):
        x=''
        for j in range(3):
            x+=board[i][j]
        if x==w:
            win=True
    #checking cols
    for j in range(3):
        x=''
        for i in range(3):
            x+=board[i][j]
        if x==w:
            win=True
    #checking diagonals
    x=''
    for i in range(3):
        x+=board[i][i]
    if x==w:
        win=True
    for i in range(3):
        x+=board[2-i][i]
    if x==w:
        win=True
    #result
    if win : #win
        return 1
    found=False
    if not win :#draw
        for i in range(3):
            if '-' in board[i]:
                found=True
        if found==False:
            return 2
        
    #continue
    return 0

def print_time(seconds):
    seconds=int(seconds)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print('Time = '+f"{hours:02d}"+':'+f"{minutes:02d}"+':'+f"{seconds:02d}") 
            

while True:
    board=[['-','-','-'],['-','-','-'],['-','-','-']]
    clear()
    print('.:: Tic Tac Toe ::.')
    print("\nChoose an option and enter it's number :")
    print("\n1. Player1 Vs Player2")
    print("2. Player Vs Computer")
    print("0. Exit")
    opt=input('option = ')

    while opt != '0'and opt !='1'and opt !='2':
        print('enter a number between 0 and 2 :')
        opt=input('option = ')
    
    if opt == '0':
        break
    elif opt == '1': #Player1 Vs Player2
        clear()
        print('.:: Tic Tac Toe ::.')
        print("| Player1 Vs Player2 |")
        t1=time()
        while True:
            #player1
            while True:
                print('\nPlayer1 :')
                row =int(input('row = '))
                col =int(input('col = '))
                if check_range(board,row,col):
                    board[row][col]='X'
                    break
            print_board(board)
            result=check_result(board,'X')
            if result==1:
                print("\n** Player1 won the game ! **")
                break
            elif result==2:
                print("\n** Result = Draw ! **")
                break
            #player2
            while True:
                print('\nPlayer2 :')
                row =int(input('row = '))
                col =int(input('col = '))
                if check_range(board,row,col):
                    board[row][col]='O'
                    break
            print_board(board)
            result=check_result(board,'O')
            if result==1:
                print("\n** Player2 won the game ! **")
                break
            elif result==2:
                print("\n** Result = Draw ! **")
                break
        sec=(time()-t1)//1
        print_time(sec)
        input("\nPress ENTER to continue ...")
    
    elif opt == '2': #Player Vs Computer   
        clear()
        print('.:: Tic Tac Toe ::.')
        print("| Player Vs Computer |")
        t1=time()
        while True:
            #player
            while True:
                print('\nPlayer :')
                row =int(input('row = '))
                col =int(input('col = '))
                if check_range(board,row,col):
                    board[row][col]='X'
                    break
            print_board(board)
            result=check_result(board,'X')
            if result==1:
                print("\n** Player won the game ! **")
                break
            elif result==2:
                print("\n** Result = Draw ! **")
                break
            #computer
            while True:
                row=random.randint(0,2)
                col=random.randint(0,2)
                if board[row][col]=='-':
                    board[row][col]='O'
                    print('\nComputer :')
                    print('row =',row)
                    print('col =',col)
                    break
            print_board(board)
            result=check_result(board,'O')
            if result==1:
                print("\n** Computer won the game ! **")
                break
            elif result==2:
                print("\n** Result = Draw ! **")
                break  
        sec=(time()-t1)//1
        print_time(sec) 
        input("\nPress ENTER to continue ...") 
