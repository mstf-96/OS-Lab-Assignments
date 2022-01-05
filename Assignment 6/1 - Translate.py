import os

WORDS = []

def load_data():
    if os.path.exists("words_bank.txt"):
        f= open('words_bank.txt','r')
        big_text=f.read()
        lines = big_text.split('\n')
        for i in range(0,len(lines)- 1,2):
            WORDS.append({'english':lines[i],'persian':lines[i+1]})
        f.close()
    else:
        print("\n[ERROR] : File 'words_bank.txt' does not exist !")
        input("\nPress ENTER to Exit...")
        exit()

#----------------------------------------------------------

def save():
    f= open('words_bank.txt','w')
    for i in range(len(WORDS)):
        f.write(WORDS[i]['english']+'\n')
        if i == len(WORDS) - 1:
            f.write(WORDS[i]['persian'])
        else:
            f.write(WORDS[i]['persian']+'\n')

    f.close()
    print("\nSaved Successfully")

#----------------------------------------------------------

def add_word():
    print('\n.:: Add new Word ::.\n')
    eng = input('Word in English : ')
    for w in WORDS:
        if w['english'] == eng:
            print("\nThis word Already exist's in Database !")
            input("\nPlease press ENTER to continue...")
            break
    else:
        per = input('Word in Persian : ')
        new_dict = {'english':eng,'persian':per}
        WORDS.append(new_dict)
        print("\nWord added successfully")
        save()
        input("\nPlease press ENTER to continue...")


#----------------------------------------------------------

def translate_en2fa():
    print('\n.:: English To Persian ::.')

    user_text = get_input_text()
    user_sentences =user_text.split('.')
    output_text=''
    for s in user_sentences:
        user_words = s.split(' ')
        output_sentence = ''
        for user_word in user_words:
            for word in WORDS:
                if user_word == word['english']:
                    output_sentence+=word['persian']+' '
                    break
            else :
                output_sentence+=user_word+' '
        output_text += output_sentence + '. '
    

    print('\nYour text in Persian :\n'+output_text)   
    input("\nPlease press ENTER to continue...")
    #return output_text

#----------------------------------------------------------

def translate_fa2en():
    print('\n.:: Persian To English ::.')
    user_text = get_input_text()
    user_sentences = user_text.split('.')
    output_text=''
    for s in user_sentences:
        user_words = s.split(' ')
        output_sentence = ''
        for user_word in user_words:
            for word in WORDS:
                if user_word == word['persian']:
                    output_sentence+=word['english']+' '
                    break
            else :
                output_sentence+=user_word+' '
        output_text += output_sentence + '. '
    
    print('\nYour text in English :\n'+output_text)
    input("\nPlease press ENTER to continue...")

#----------------------------------------------------------

def get_input_text():
    print('\nPlease enter the text you want to be translated :')
    return input('input text = ')

#----------------------------------------------------------

def menu():
    print("\n.:: Translator ::.\n")
    print("Please select an option and enter it's number :\n")
    print('1. Add new word')
    print('2. Translate English to Persian')
    print('3. Translate Persian to English')
    print('4. Exit')

    choice = int(input("\nYour choice = "))
    while not (1<= choice <= 4):
        print("Please enter a number between 1 and 4")
        choice = int(input("Your choice = "))
    
    return choice

#----------------------------------------------------------

load_data()
while True:
    choice = menu()
    if choice == 1:
        add_word()
    elif choice == 2:
        translate_en2fa()
    elif choice == 3:
        translate_fa2en()
    elif choice == 4:
        print("\nGoodbye!\n")
        break