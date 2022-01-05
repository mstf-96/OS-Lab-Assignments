from random import choice
from os import system, name

def clear():
      if name == 'nt':
        _ = system('cls')
      else:
        _ = system('clear')

words_list = ['apple','door','orange','ball','bell','python','linux','ubuntu','windows','time','boy','girl']
exit=0
while True:

    word = choice(words_list)
    l=len(word)
    health = 7
    guessed =''
    
    if exit==1:
        break
    
    while health>0:

        print('.:: Hangman Game ::.')
        print('Health =',health)
        print('Word = ',end='')
        for i in range(l):
            if word[i] in guessed :
                print(word[i],end='')
            else:
                print('-',end='')
        print('\n')
        char=input('Enter a character : ')
        while len(char)!=1:
            print("Please enter just one character !")
            char=input('Enter a character : ')
        char=char.lower()

        if char in word and char not in guessed:
            print('YES it is in word')
            guessed+=char
        elif char in word and char in guessed:
            print('You have already guessed this character!')
        else:
            print('NO it is NOT in word')
            health-=1
        

        if health==0:
            print('GAME OVER !')
            exit=1
        
        win=True
        for i in range(l):
            if word[i] not in guessed:
                win=False
                break
        
        if win:
            print('Congratulations You WON !')
            exit=1
            health=0
        print('Word = ',end='')

        for i in range(l):
            if word[i] in guessed :
                print(word[i],end='')
            else:
                print('-',end='')
        print('\n')


        input('\nPress ENTER to continue ...')
        clear()


    












