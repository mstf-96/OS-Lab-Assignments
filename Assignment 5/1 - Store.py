
PRODUCTS = []

def load_data_from_file():
    print('\nLoading...')
    file = open('database.csv','r')

    for row in file:
        info = row[:-1].split(',')
        new_dict = {'code':info[0] , 'name':info[1] , 'price':info[2] , 'count':info[3]}
        PRODUCTS.append(new_dict)
    file.close()
    show_list()
    print("\nDataBase Loaded Successfully")

#-------------------------------------------

def search_index_by_name(product_name):
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['name']==product_name:
            return i
    return -1

#-------------------------------------------

def search_index_by_code(product_code):
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['code']==product_code:
            return i
    return -1

#-------------------------------------------

def get_code():
    code = input("Please enter product's code : ")
    while search_index_by_code(code) != -1:
        print('This code belongs to another product. Try again.')
        code = input("Please enter product's code : ")
    return code

#-------------------------------------------

def get_price():
    price = int(input("Please enter product's price : "))
    while price<=0:
        print('Please enter a positive integer.')
        price = int(input("Please enter product's price : "))
    return price

#-------------------------------------------

def get_count():
    count = int(input("Please enter product's count : "))
    while count<0:
        print('Please enter a none negetive integer.')
        count = int(input("Please enter product's count : "))
    return count

#-------------------------------------------

def add():
    while True:
        print('\n.:: Add ::.\n')
        print("  1. Add a product to database")
        print("  2. Go back to main menu")
        
        choice =int(input('\nPlease enter your choice : '))
        while(choice!=1 and choice != 2):
            print('Please enter 1 or 2')
            choice =int(input('Please enter your choice : '))
            
        if choice==1: 
            name = input("\nPlease enter product's name : ")
            i = search_index_by_name(name)
            if i == -1:
                code = get_code()
                price = get_price()
                count = get_count()
                new_dict = {'code':code , 'name':name , 'price':price , 'count':count}
                PRODUCTS.append(new_dict)
                print("\nProduct added successfully")
            else:
                print('\nThis product has been added before.')
                print("\nProduct info : code =",PRODUCTS[i]['code'],"name =",PRODUCTS[i]['name'],"price =",PRODUCTS[i]['price'],"count =",PRODUCTS[i]['count'])
                print("\nDo you want to change it's count ? [y/n]")
                answer=input("your choice = ")
                while answer!='y' and answer !='n':
                    print('please enter y or n')
                    answer=input("your choice = ")
                if answer=='y':
                    PRODUCTS[i]['count'] = get_count()
                    print("\nProduct count changed successfully")
            input("\nPress ENTER to continue...")
        elif choice==2:
            break
        
#-------------------------------------------

def edit():
    while True:
        print('\n.:: Edit ::.')
        print("  1. Edit a product in database")
        print("  2. Go back to main menu")
            
        choice =int(input('\nPlease enter your choice : '))
        while(choice!=1 and choice != 2):
            print('Please enter 1 or 2')
            choice =int(input('Please enter your choice : '))
                
        if choice==1:
            name = input("\nPlease enter product's name : ")
            i = search_index_by_name(name)
            if i==-1:
                print("There is no product with this name in database. You can add it by going to add menu")
            else:
                print("\nProduct info : code =",PRODUCTS[i]['code'],"name =",PRODUCTS[i]['name'],"price =",PRODUCTS[i]['price'],"count =",PRODUCTS[i]['count'])
                print("\nPlease enter this product's new info :\n")

                name = input("Please enter product's name : ")
                j = search_index_by_name(name)
                while j != -1 and j != i :
                    print('This name belongs to another product. Try again.')
                    code = input("Please enter product's name : ")
                
                code = input("Please enter product's code : ")
                j = search_index_by_code(code)
                while j != -1 and j != i :
                    print('This code belongs to another product. Try again.')
                    code = input("Please enter product's code : ")
                
                price = get_price()
                count = get_count()
                PRODUCTS[i]['code'] = code
                PRODUCTS[i]['name'] = name
                PRODUCTS[i]['price'] = price
                PRODUCTS[i]['count'] = count
                print("\nProduct info has been changed successfully")
            input("\nPress ENTER to continue...")
        elif choice==2:
            break

#-------------------------------------------

def delete():
    while True:
        print('\n.:: Delete ::.')
        print("  1. Delete a product from database")
        print("  2. Go back to main menu")
            
        choice =int(input('\nPlease enter your choice : '))
        while(choice!=1 and choice != 2):
            print('Please enter 1 or 2')
            choice =int(input('Please enter your choice : '))
                
        if choice==1:
            name = input("\nPlease enter product's name : ")
            i = search_index_by_name(name)
            if i==-1:
                print("\nThere is no product with this name in database.")
            else:
                print("\nProduct info : code =",PRODUCTS[i]['code'],"name =",PRODUCTS[i]['name'],"price =",PRODUCTS[i]['price'],"count =",PRODUCTS[i]['count'])
                PRODUCTS.pop(i)
                print("\nProduct deleted successfully")
            input("\nPress ENTER to continue...")
        
        elif choice==2:
            break

#-------------------------------------------

def show_list():
    print('\nCode\t\tName\t\tPrice\t\tCount')
    for product in PRODUCTS:
        print(product['code'],'\t\t',product['name'],'\t\t',product['price'],'\t\t',product['count'])
    

#-------------------------------------------

def search():
    print('\n.:: Search ::.')
    name = input("\nPlease enter product's name : ")
    i = search_index_by_name(name)
    if i==-1:
        print("\nThere is no product with this name in database.")
    else:
        print("\nProduct info : code =",PRODUCTS[i]['code'],", name =",PRODUCTS[i]['name'],", price =",PRODUCTS[i]['price'],", count =",PRODUCTS[i]['count'])
    input("\nPress ENTER to continue...")

#-------------------------------------------

def buy():
    shop_list=[]
    while True:
        print("\n.:: Buy ::.\n")
        print("  1. Add a product to cart")
        print("  2. Finish shopping and see Factor")
        print("  3. Show List")
        choice =int(input('Please enter your choice : '))
        while(choice!=1 and choice != 2 and choice != 3):
            print('Please enter 1 or 2 or 3')
            choice =int(input('Please enter your choice : '))
        
        if choice==1: 
            name = input("Please enter product's name : ")
            i = search_index_by_name(name)
            if i==-1:
                print("\nThere is no product with this name in database.")
            else:
                print("Product info : code =",PRODUCTS[i]['code'],"name =",PRODUCTS[i]['name'],"price =",PRODUCTS[i]['price'],"count =",PRODUCTS[i]['count'])
                count = int(input("How many do you want to Buy : "))
                while count<0 or count > int(PRODUCTS[i]['count']):
                    if count<0 :
                        print('Please enter a none negetive integer.')
                    if count > int(PRODUCTS[i]['count']):
                        print('There is only',PRODUCTS[i]['count'],PRODUCTS[i]['name'],'available')
                    count = int(input("How many do you want to Buy : "))
                
                if count != 0:
                    new_dict = {'name':PRODUCTS[i]['name'],'price':PRODUCTS[i]['price'],'count':count}
                    shop_list.append(new_dict)
                    PRODUCTS[i]['count'] = int(PRODUCTS[i]['count']) - count
                    print("\nProduct successfully added a  to cart")
                input("\nPress ENTER to continue...")
        
        elif choice == 2:
            if len(shop_list)==0:
                print("\nYour Shopping cart is empty. You didn't buy anything.")
            else:
                total_cost = 0 
                print("\n.:: Factor ::.")
                print('\nCount\t\tName\t\tPrice')
                for item in shop_list:
                    print(item['count'],'\t\t',item['name'],'\t\t',item['price'])
                    total_cost += int(item['count']) * int(item['price'])
                
                print("\nTotal Cost =",total_cost)
            input("\nPress ENTER to continue...")
            break
        elif choice == 3:
            show_list()

#-------------------------------------------

def save():
    file=open('database.csv','w')
    line=''
    for product in PRODUCTS:
        line = str(product['code'])+','+str(product['name'])+','+str(product['price'])+','+str(product['count'])+'\n'
        file.write(line)
    file.close()
    print('\nSaved successfully.')

#-------------------------------------------

def show_menu():
    print("""\n.:: Welcome to Store ::.
    1. Add
    2. Edit
    3. Delete
    4. Show List
    5. Search
    6. Buy
    0. Save and Exit""")

#-------------------------------------------


load_data_from_file()

while(True):
    show_menu()
    choice =int(input('Please enter your choice : '))
    while(choice<0 or 6 < choice):
        print('Please enter a number between 0 and 6')
        choice =int(input('Please enter your choice : '))
    
    if choice == 1:
        add()
        save()
    elif choice == 2:
        edit()
        save()
    elif choice == 3:
        delete()
        save()
    elif choice == 4:
        show_list()
    elif choice == 5:
        search()
    elif choice == 6:
        buy()
    elif choice == 0:
        save()
        print('\nGoodbye !\n')
        exit()