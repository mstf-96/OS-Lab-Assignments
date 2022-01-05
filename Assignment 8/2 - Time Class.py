class Time:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.fix()
    
    def fix(self):
        if 60 <= self.second :
            self.minute += self.second // 60
            self.second %= 60
        elif self.second < 0 : 
            self.minute -= (abs(self.second) // 60) + 1
            self.second += ((abs(self.second) // 60) + 1) * 60

        if 60 <= self.minute:
            self.hour += self.minute // 60
            self.minute %= 60
        elif self.minute < 0 : 
            self.hour -= (abs(self.minute) // 60) + 1
            self.minute += ((abs(self.minute) // 60) + 1) * 60
        
    def __add__(self,other):
        if not isinstance(other, Time):
            raise TypeError
        result = Time()
        result.second = self.second + other.second
        result.minute = self.minute + other.minute
        result.hour = self.hour + other.hour
        result.fix()
        return result
    
    def __sub__(self,other):
        if not isinstance(other, Time):
            raise TypeError
        s = self.time_2_seconds() - other.time_2_seconds()
        if s<0 :
            s=abs(s)
        result = Time.seconds_2_time(s)
        return result

    def time_2_seconds(self):
        result = self.second + self.minute * 60 + self.hour * 3600
        return result

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    
    @staticmethod
    def seconds_2_time(seconds):
        result = Time()
        result.second = seconds
        result.fix()
        return result
    
#-------------------------------------------------------------------

def get_time():
    h = int(input('Hour = '))
    while h < 0:
        print('Please enter a positive number !')
        h = int(input('Hour = '))
    
    m = int(input('Minute = '))
    while m < 0:
        print('Please enter a positive number !')
        m = int(input('Minute = '))
    
    s = int(input('Second = '))
    while s < 0:
        print('Please enter a positive number !')
        s = int(input('Second = '))
    
    return Time(h,m,s)

#-------------------------------------------------------------------

while True:
    print('.:: Time ::.\n')
    print('1. Add \n2. Subtract \n3. Time to Seconds\n4. Seconds to Time\n5. Exit')
    opt=int(input('Your choice = '))
    
    while not (1 <= opt <=5):
        print('Please enter a number between 1 and 5 !')
        opt=int(input('Your choice = '))
    
    if opt==5:
        print('\nGoodbye !\n')
        break

    if opt==1 or opt==2 :
        print('\nEnter Time 1 :')
        a = get_time()
        print(a)
        print('\nEnter Time 2 :')
        b = get_time()
        if opt==1 :
            print(a,'+',b,'=', a + b)
        elif opt==2:
            print(a,'-',b,'=', a - b)
    elif opt==3:
        print('\nEnter Time :')
        a = get_time()
        print('Seconds =',a.time_2_seconds())
    elif opt==4:
        seconds = int(input('\nSeconds = '))
        while seconds < 0:
            print('Please enter a positive number.')
            seconds = int(input('Seconds = '))
        print("Time =",Time.seconds_2_time(seconds))
    input('\nPress ENTER to Continue...\n')