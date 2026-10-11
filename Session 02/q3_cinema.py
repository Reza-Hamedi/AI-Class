import os
import time

weekdays = {0: "Saturday", 1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday"}
def calculate_discount(price):
   discount_applied = price - (price * 0.20) if isinstance(price, int) else price
   return discount_applied

def issue_invoice(tickets, user_name):
    time.sleep(2)
    print("System is issuing invoice ..." )
    time.sleep(3)
    os.system('cls')
    print(f"$ Tickets Invoice $ \tUser Name : {user_name} \t User Address: Non")
    print("_" * 50)
    for t in tickets:
        print(f"Audience Name : {t.get('name')}")
        print(f"Day : {weekdays.get(t.get('date'))}")
        if t.get("date") == 3:
            discount_applied  =  calculate_discount( t.get('price'))
            print(f"Original price: {t.get('price')} | 20% discount applied {discount_applied}")
        else:
            print(f"Original price: {t.get('price')}")
        print("*" * 50)

        

def display_current_day(current_day):
    has_discount = False
    if current_day == 3:
        has_discount = True
        print("Congratulations! Today is Tuesday, and all tickets are 20%\ off.")
    elif current_day == -1:
        pass
    else:
        print(f"Today is {weekdays.get(current_day)}.")
    return has_discount

def calculate_price(tickets):
    for t in tickets:
        age = t.get("age")
        if age > 0 and age <= 5:
            t["price"] = "Free"
        elif age >= 6 and age <= 12:
            t["price"] = 50000
        elif age > 60:
            t["price"] = 60000
        else:
            t["price"] = 100000


def getUserInformation():
    tickets = []
    user_name = ""
    number_of_tickets = 0

    # نام کاربر اصلی
    while not user_name:
        user_name = input("Welcome dear user :) \nplease enter your name ...\n Name :  ")
        os.system('cls')
    print(f"Welcome {user_name}")

    # تعداد بلیط درخواستی
    while number_of_tickets == 0:
        number_of_tickets = int(input("How many tickets do you want? "))
        os.system('cls')
    print(f"You want {number_of_tickets} tickets.")

    # پر کردن اطلاعات بلیط ها
    for i in range(1, number_of_tickets + 1):
        tickets.append({"name": input(f"{i}. Audience Name : "),
                        "age": int(input(f"{i} Audience Age : ")),
                        "date":  int(input(f"{i}. Which day? \n (0: Saturday, 1: Sunday, 2: Monday, 3: Tuesday, 4: Wednesday, 5: Thursday, 6: Friday)  "))})

    return tickets, user_name



# ................................
def userController():
    user_type = ""
    current_day = -1
    is_admin = False
    while not user_type:
        user_type =input("Are you an Admin or a Regular User?\nAdmin --> admin \nRegular User --> user\nNote: isn't case sensitive !!\n")
        os.system('cls')

    if user_type.lower() == "admin":
        print("Welcome, Admin :)")
        while current_day == -1:
            for key, value in weekdays.items():
                print(f"{value} : {key}")
            current_day = int(input("Please specify the date (1 - 7): "))
            if  0 <= current_day < 7:
                pass                
            else:
                current_day = -1
            os.system('cls')

        is_admin = True
    elif user_type.lower() == "user":
        print("Welcome, User!")
    else:
        os.system('cls')
        print("Invalid role!")
        userController()
    return current_day, is_admin
# ................................

def main():
    os.system('cls')
    current_day, is_admin = userController()
        
    # بررسی و نمایش روز جاری
    has_discount = display_current_day(current_day)
    
    if is_admin: # ادمین لاگین کرده است
        tickets, user_name = getUserInformation()
        calculate_price(tickets)
        issue_invoice(tickets, user_name)
        
        
    else:   # ادمین لاگین نکرده است
        time.sleep(2)
        print("System are loading fundamental configs ... ")
        time.sleep(2)
        print("Fetching data ...")
        time.sleep(2)
        print("Admin has not specified the date :( ")
        time.sleep(2)
        print('''Please ask the Admin to log in first and set the current day;
            You will then be logged in automatically :( ''')
        time.sleep(6)
        main()


main()