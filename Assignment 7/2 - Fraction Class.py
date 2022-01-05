import math

class Kasr:

    def __init__(self,soorat,makhraj):
        self.soorat = soorat
        self.makhraj = makhraj
    
    def sade_sazi(self):
        bmm = math.gcd(self.soorat , self.makhraj)
        if bmm != 0:
            self.soorat = self.soorat // bmm
            self.makhraj = self.makhraj // bmm
        return self

    def __add__(self , other):
        javab_soorat = self.soorat * other.makhraj + other.soorat * self.makhraj
        javab_makhraj = self.makhraj * other.makhraj
        return Kasr(javab_soorat , javab_makhraj).sade_sazi()
    
    def __sub__(self , other):
        javab_soorat = self.soorat * other.makhraj - other.soorat * self.makhraj
        javab_makhraj = self.makhraj * other.makhraj
        return Kasr(javab_soorat , javab_makhraj).sade_sazi()
    
    def __mul__(self , other):
        javab_soorat = self.soorat * other.soorat
        javab_makhraj = self.makhraj * other.makhraj
        return Kasr(javab_soorat , javab_makhraj).sade_sazi()
    
    def __truediv__(self , other):
        javab_soorat = self.soorat * other.makhraj
        javab_makhraj = self.makhraj * other.soorat
        return Kasr(javab_soorat , javab_makhraj).sade_sazi()
    
#    def __repr__(self):
#         return str(self.soorat) + '/' + str(self.makhraj)
    
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
    print('1. Jam (+)\n2. Tafrigh (-)\n3. Zarb (*)\n4. Taghsim (/)\n5. Exit')
    opt=int(input('Entekhabe Shoma = '))
    
    while not (1 <= opt <=5):
        print('Yek adad bein 1 ta 5 vared konid !')
        opt=int(input('Entekhabe Shoma = '))
    
    if opt==5:
        print('\nGoodbye !\n')
        break

    print('\nKasr avval :')
    a = get_kasr()
    print(a)
    print('\nKasr dovvom :')
    b = get_kasr()
    print()
    if opt==1:
        print(a,'+',b,'=', a + b)
    elif opt==2:
        print(a,'-',b,'=', a - b)
    elif opt==3:
        print(a,'*',b,'=', a * b)
    elif opt==4:
        print(a,'/',b,'=', a / b)
    input('\nPress ENTER to Continue...\n')