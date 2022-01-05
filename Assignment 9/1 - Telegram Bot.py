import telebot
import random
import qrcode
import khayyam
import gtts
import os


bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "سلام " + message.from_user.first_name + "\nبه بات من خوش اومدي.")

#-------------------------------------------------------------------------------------------------

random_number = 0

@bot.message_handler(commands=['game'])
def game(message):
    bot.reply_to(message,"بازي حدس عدد :\nبرای خروج از بازی بنویس : exit")
    global random_number
    random_number = random.randint(0,100)
    user_answer = bot.send_message(message.chat.id, "يك عدد بين 0 تا 100 حدس بزن :")
    bot.register_next_step_handler(user_answer, guess_number)  

def guess_number(user_answer):
    global random_number
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    button = telebot.types.KeyboardButton('New Game')
    markup.add(button)

    if user_answer.text=='exit':
        bot.send_message(user_answer.chat.id, 'شما از بازی خارج شدین',reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
    elif user_answer.text == "New Game":
        user_answer = bot.send_message(user_answer.chat.id, 'بازی جدید :\nیک عدد بین 0 تا 100 حدس بزن :',reply_markup=markup)
        random_number = random.randint(0,100)
        bot.register_next_step_handler(user_answer, guess_number)
    else:
        try:
            if int(user_answer.text) < random_number:
                user_answer = bot.send_message(user_answer.chat.id, 'برو بالا', reply_markup=markup)
                bot.register_next_step_handler(user_answer, guess_number)
            elif int(user_answer.text) > random_number:
                user_answer = bot.send_message(user_answer.chat.id, 'برو پایین', reply_markup=markup)
                bot.register_next_step_handler(user_answer, guess_number)
            elif int(user_answer.text) == random_number:
                markup = telebot.types.ReplyKeyboardRemove(selective=True)
                bot.send_message(user_answer.chat.id, "آفرين برنده شدي !", reply_markup=markup)
        except:
            user_answer = bot.send_message(user_answer.chat.id, "لطفا عدد صحیح وارد کن", reply_markup=markup)
            bot.register_next_step_handler(user_answer, guess_number)

#-------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['age'])
def age(message):
    age = bot.send_message(message.chat.id, 'تاریخ نولدت رو به صورت مقابل وارد کن : 1388/8/8')
    bot.register_next_step_handler(age, age_calculation)

def age_calculation(message):
    try:
        birth_day = message.text.split("/")
        dif = str(khayyam.JalaliDatetime.now() - khayyam.JalaliDatetime(birth_day[0], birth_day[1], birth_day[2]))
        dif = dif.split(' ')
        year = int(dif[0])//365
        day= int(dif[0])%365
        
        bot.send_message(message.chat.id, "شما "+str(year)+" سال و "+str(day)+" روز سن دارید")
    except:
        age = bot.send_message(message.chat.id,"لطفا تاریخ تولدت رو به صورت گفته شده وارد کن")
        bot.register_next_step_handler(age, age_calculation)

#-------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['voice'])
def voice_generat_function(message):
   txt = bot.send_message(message.chat.id,"یک جمله انگلیسی بفرست. مثلا : hello i am mostafa")
   bot.register_next_step_handler(txt, text2voice)

def text2voice(message):
    try:
        text = message.text
        obj = gtts.gTTS(text=text, lang='en', slow=False)
        obj.save("voice.mp3")
        voice = open('voice.mp3', 'rb')
        bot.send_voice(message.chat.id, voice)
        voice.close()
        os.remove("voice.mp3")
    except:
        txt = bot.send_message(message.chat.id,"لطفا فقط متن انگلیسی بفرست")
        bot.register_next_step_handler(txt, text2voice)

#-------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['max'])
def max_handle(message):
    bot.send_message(message.chat.id,message.text)
    user_input = bot.send_message(message.chat.id , "یک آرایه از اعداد به صورت مقابل بفرست : 5,4,10,15")
    bot.register_next_step_handler(user_input, max_finder)

def max_finder(message):
    try:
        nums = list(map(int, message.text.split(',')))
        max_number =max(nums)
        bot.send_message(message.chat.id, "بزرگترین عدد : " + str(max_number))
    except:
        user_input = bot.send_message(message.chat.id,"لطفا اعداد رو فقط به صورت گفته شده بفرست")
        bot.register_next_step_handler(user_input, max_handle)
    

#-------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['argmax'])
def argmax(message):
    user_input = bot.send_message(message.chat.id, "یک آرایه از اعداد به صورت مقابل بفرست : 5,4,10,15")
    bot.register_next_step_handler(user_input, max_index_finder)

def max_index_finder (message):
    try:
        numbers = list(map(int, message.text.split(',')))
        max_index = numbers.index(max(numbers)) + 1
        bot.send_message(message.chat.id, "عدد " + str(max_index) + " ام بزرگترین عدد است")
    except:
        user_input = bot.send_message(message.chat.id,"لطفا اعداد رو فقط به صورت گفته شده بفرست")
        bot.register_next_step_handler(user_input, argmax)


#-------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['qrcode'])
def qr(message):
    txt = bot.send_message(message.chat.id, 'لطفا نوشته خود را وارد کنید ')
    bot.register_next_step_handler(txt, produce_qrcode)

def produce_qrcode(message):
    qr_image = qrcode.make(message.text)
    qr_image.save('qr_code.png')
    pic = open('qr_code.png', 'rb')
    bot.send_photo(message.chat.id, pic)
    pic.close()
    os.remove('qr_code.png')

#-------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['help'])
def help_function(message):
    bot.reply_to(message,""""
/start : خوش آمد گویی
/game : بازی حدس عدد
/age : محاسبه سن
/voice : تبدیل جمله انگلیسی به صدا
/max : پیدا کردن بزرگترین عدد یک آرایه 
/argmax : پیدا کردن اندیس بزرگترین عدد
/qrcode : تبدیل متن به Qr-Code  
/help : نمایش دستورات و عملکرد آنها""" )

#-------------------------------------------------------------------------------------------------

bot.infinity_polling()