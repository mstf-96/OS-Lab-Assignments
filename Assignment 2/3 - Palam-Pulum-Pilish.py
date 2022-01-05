import random
from os import system, name

def clear():
      if name == 'nt':
        _ = system('cls')
      else:
        _ = system('clear')

while True:
    i=1
    user_score = 0
    computer1_score = 0
    computer2_score = 0
    while i<=5:

        print('.:: ROUND '+str(i)+' ::.')
        print("Choose one of the options and enter it's number :")
        print('1. Palm of hand')
        print('2. Back of hand')
        print('0. Exit')
        opt = input('Your choice = ')
        while opt != '0' and opt != '1' and opt != '2':
            print("Invalid input ! . Please Choose one of the options and enter it's number :")
            opt = input('Your choice = ')

        if opt == '0':
            print('Goodbye !')
            exit()
        elif opt == '1':
            user = 'Palm'
        elif opt == '2':
            user = 'Back'

        pc1 = random.randint(1, 2)
        pc2 = random.randint(1, 2)

        if pc1 == 1:
            pc1 = 'Palm'
        elif pc1 == 2:
            pc1 = 'Back'
        
        if pc2 == 1:
            pc2 = 'Palm'
        elif pc2 == 2:
            pc2 = 'Back'

        print('-----------------------------------------')
        print("User : " + user)
        print("Computer 1 : " + pc1)
        print("Computer 2 : " + pc2)
        print('-----------------------------------------')


        if user == pc1 and pc1 == pc2:
            print('Round result : Tie')

        elif (user=="Palm" and pc1=="Back" and pc2=="Back") or (user=="Back" and pc1=="Palm" and pc2=="Palm"):
            user_score += 1
            print('Round result : User won !')
            
        elif (user=="Palm" and pc1=="Back" and pc2=="Palm") or (user=="Back" and pc1=="Palm" and pc2=="Back"):
            computer1_score += 1
            print('Round result : Computer 1 won !')
                        
        elif (user=="Palm" and pc1=="Palm" and pc2=="Back") or (user=="Back" and pc1=="Back" and pc2=="Palm"):
            computer2_score += 1
            print('Round result : Computer 2 won !')
        
        print('-----------------------------------------')
        print("User score =",user_score)
        print("Computer 1 score =",computer1_score)
        print("Computer 2 score =",computer2_score)
        
        if i == 5 :
            if computer1_score < user_score and computer2_score < user_score:
                print('Game result : User won the Game !')
            elif user_score < computer1_score and computer2_score < computer1_score:
                print('Game result : Computer 1 won the Game !')
            elif user_score < computer2_score and computer1_score < computer2_score:
                print('Game result : Computer 2 won the Game !')
            else:
                print("Game result : It's a tie !")

        i += 1

        print('-----------------------------------------')
        input('Press ENTER to continue ... ')
        clear()


