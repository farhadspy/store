#store

PRODUCTS = []
my_dict = {}

def read_from_database():
    f = open("store/database.txt","r")
    
    for line in f:
        line = line.strip()  # حذف فاصله‌ها و اینترها
        if not line:  # نادیده گرفتن خطوط خالی
            continue
        result = line.split(",")
        my_dict = {"code":result[0] ,
                   "name":result[1] ,
                   "price":result[2] ,
                   "count":result[3]}
        
        PRODUCTS.append(my_dict)
        
        f.close

def write_to_database():
    file = open("store/database.txt", "w")
    for product in PRODUCTS:
        if all(key in product for key in ["code", "name", "price", "count"]):
            file.write(f"{product['code']},{product['name']},{product['price']},{product['count']}\n")

def sort():
    PRODUCTS.sort(key= lambda x: int(x["code"]))
    
def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show List")
    print("6- Buy")
    print("7- Exit")
    
def add():
    while True:
        code = int(input("enter code: "))
        name = input("enter name: ")
        for product in PRODUCTS:
            if int(product["code"]) == code:
                print("the code is exist.")
                break
            elif product["name"] == name:
                print("the name is exist.")
                break
        else:
            price = input("enter price: ")  
            count = int(input("enter count: "))
            break 
    new_product = {"code":code , "name":name , "price":price , "count":count}
    PRODUCTS.append(new_product)

def edit():
    while True:
        edit_list = search()
        if edit_list != None:
            edit_list["name"] = input("pls enter name: ")
            edit_list["price"] = input("pls enter price: ")
            edit_list["count"] = input("pls enter count: ")
            break 
    for product in PRODUCTS:
        if product["code"] == edit_list["code"] or product["name"] == edit_list["name"]:
            product.update({"name":edit_list["name"] , "price":edit_list["price"] , "count":edit_list["count"]})
    
def remove():
    while True:
        remove_from_list = search() 
        if remove_from_list != None:
            for product in PRODUCTS:
                if product["code"] == remove_from_list["code"] or product["name"] == remove_from_list["name"]:
                    PRODUCTS.remove(product)
                    break
            break
    
def search():
    user_input = input("type your keyword: ")  
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"],"\t\t" , product["name"],"\t\t" , product["price"],"\t\t" ,product["count"],"\t\t" )
            token = 1
            return product
    else:
        print("not found")
        token = -1
        
def show_list():
    sort()
    print("code\t\tname\t\t\tprice\t\tcount") 
    for product in PRODUCTS:
        print(product["code"], "\t\t" , product["name"], "\t\t\t" , product["price"]) 
         
def buy():
    while True:
        buy_items = search()
        number_of_buy = int(input("how much do you want: "))
        
        for product in PRODUCTS:
            if product["name"] == buy_items["name"]:
                if int(product["count"]) >= number_of_buy:
                    product["count"] = str(int(product["count"]) - number_of_buy)
                else:
                    print("Limited stock. Stock is ", product["count"] ," pieces.")
        finish_buy = input("if your buying is finish enter yes else enter no: ")
        if finish_buy == "yes":
            break
        else:
            continue


print("Welcome to farhad store")
print("Loading...")
read_from_database()
print("Data Loading.")

while True:
    
    show_menu()
    choice = int(input("enter number: "))
    
    if choice == 1 :
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        sort()
        write_to_database()
        exit(0)
    else:
        print("wrong number.pls enter corect number.")