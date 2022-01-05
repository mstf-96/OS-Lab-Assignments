import math

class Kasr:

    def __init__(self,soorat=0,makhraj=1):
        self.soorat = soorat
        self.makhraj = makhraj
    
    def sade_sazi(self):
        bmm = math.gcd(self.soorat , self.makhraj)
        if bmm != 0:
            self.soorat = self.soorat // bmm
            self.makhraj = self.makhraj // bmm

    def __add__(self , other):
        javab = Kasr()
        javab.soorat = self.soorat * other.makhraj + other.soorat * self.makhraj
        javab.makhraj = self.makhraj * other.makhraj
        javab.sade_sazi()
        return javab
    
    def __sub__(self , other):
        javab = Kasr()
        javab.soorat = self.soorat * other.makhraj - other.soorat * self.makhraj
        javab.makhraj = self.makhraj * other.makhraj
        javab.sade_sazi()
        return javab
    
    def __mul__(self , other):
        javab = Kasr()
        javab.soorat = self.soorat * other.soorat
        javab.makhraj = self.makhraj * other.makhraj
        javab.sade_sazi()
        return javab
    
    def __truediv__(self , other):
        javab = Kasr()
        javab.soorat = self.soorat * other.makhraj
        javab.makhraj = self.makhraj * other.soorat
        javab.sade_sazi()
        return javab
    
    
    def __str__(self):
         return str(self.soorat) + '/' + str(self.makhraj)

#-------------------------------------------------------------------

def get_kasr():
    s = int(input('soorat = '))
    m = int(input('makhraj = '))
    while m == 0:
        print('makhraj nemitavanad 0 bashad !')
        m = int(input('makhraj = '))
    return Kasr(s,m)

#-------------------------------------------------------------------

while True:
    print('.:: Kasr ::.\n')
    print('1. Jam (+)\n2. Tafrigh (-)\n3. Zarb (*)\n4. Taghsim (/)\n5. Sade sazi \n6. Exit')
    opt=int(input('Entekhabe Shoma = '))
    
    while not (1 <= opt <=6):
        print('Yek adad bein 1 ta 6 vared konid !')
        opt=int(input('Entekhabe Shoma = '))
    
    if opt==6:
        print('\nGoodbye !\n')
        break
    
    if 1<=opt<=4:
        print('\nKasr avval :')
        a = get_kasr()
        print(a)
        print('\nKasr dovvom :')
        b = get_kasr()
        print(b)
    if opt==1:
        print(a,'+',b,'=', a + b)
    elif opt==2:
        print(a,'-',b,'=', a - b)
    elif opt==3:
        print(a,'*',b,'=', a * b)
    elif opt==4:
        print(a,'/',b,'=', a / b)
    elif opt==5:
        a=get_kasr()
        a.sade_sazi()
        print('\nSade shode kasr =',a)
    input('\nPress ENTER to Continue...\n')