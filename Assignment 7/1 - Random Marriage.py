import random

boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']

n = min(len(boys),len(girls))
couples=[]

for i in range(n):
    random_boy = random.randint(0,len(boys)-1)
    random_girl = random.randint(0,len(girls)-1)
    new_dict = {'boy':boys[random_boy],'girl':girls[random_girl]}
    couples.append(new_dict)
    boys.pop(random_boy)
    girls.pop(random_girl)

print("\nMarried Couples :\n")
for i in range(n):
    print('Couple',i+1,':',couples[i]['boy'],',',couples[i]['girl'])

if len(boys) != 0:
    print('\nSingle Boys :\n')
    for i in range(len(boys)):
        print(boys[i])

if len(girls) != 0:
    print('\nSingle Girls :\n')
    for i in range(len(girls)):
        print(girls[i])