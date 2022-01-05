import random
from os import system, name
from time import sleep

def clear():
      if name == 'nt':
        _ = system('cls')
      else:
        _ = system('clear')

while True:
    i=1
    user_score = 0
    computer_score = 0

    while i<=5:

        print('.:: ROUND '+str(i)+' ::.')
        print("Choose one of the options and enter it's number :")
        print('1. Rock')
        print('2. Paper')
        print('3. Scissors')
        print('0. Exit')
        opt = input('Your choice = ')
        while opt != '0' and opt != '1' and opt != '2' and opt != '3':
            print("Invalid input ! . Please Choose one of the options and enter it's number :")
            opt = input('Your choice = ')

        if opt == '0':
            print('Goodbye !')
            exit()

        computer_choice = random.randint(1, 3)

        if computer_choice == 1:
            computer_choice = 'Rock'
        elif computer_choice == 2:
            computer_choice = 'Paper'
        elif computer_choice == 3:
            computer_choice = 'Scissors'

        if opt == '1':
            user_choice = 'Rock'
        elif opt == '2':
            user_choice = 'Paper'
        elif opt == '3':
            user_choice = 'Scissors'
        
        print('-----------------------------------------')


        print("User : " + user_choice)
        print("Computer : " + computer_choice)


        if computer_choice == user_choice :
            print('Round result : Tie')
        elif computer_choice == 'Rock' and user_choice == 'Paper':
            user_score += 1
            print('Round result : User won !')
        elif computer_choice == 'Paper' and user_choice == 'Rock':
            computer_score += 1
            print('Round result : Computer won !')

        elif computer_choice == 'Rock' and user_choice == 'Scissors':
            computer_score += 1
            print('Round result : Computer won !')
        elif computer_choice == 'Scissors' and user_choice == 'Rock':
            user_score += 1
            print('Round result : User won !')

        elif computer_choice == 'Paper' and user_choice == 'Scissors':
            user_score += 1
            print('Round result : User won !')
        elif computer_choice == 'Scissors' and user_choice == 'Paper':
            computer_score += 1
            print('Round result : Computer won !')

        print('-----------------------------------------')
        print("User score =",user_score)
        print("Computer score =",computer_score)
        
        if i == 5 :
            if computer_score > user_score:
                print('Game result : Computer won the Game !')
            elif computer_score < user_score:
                print('Game result : User won the Game !')
            else:
                print("Game result : It's a tie !")

        i += 1

        print('-----------------------------------------')
        input('Press ENTER to continue ... ')
        # sleep(5)
        clear()
