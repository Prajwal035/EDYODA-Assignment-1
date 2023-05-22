import sys
from admin import *
from user import *

print("Welcome to Food Ordering App  ")
while True:
    role=int(input("Enter the role for food ordering App \n1.Admin\n2 User\n3 Exit\n"))
    if role==1:
        res=admin()
        while True:
            print("Press 1 for add food items ")
            print("Press 2 for edit food items ")
            print("Press 3 for remove add food items ")
            print("Press 4 for view add food items ")
            print("Press 0 for exit food items ")
            admin_input=int(input("Enter the your preference "))
            if admin_input==1:
                res.add_food_items()
            elif admin_input==2:
                res.edit_food_items()
            elif admin_input==3:
                res.remove_food()
            elif admin_input==4:
                res.view_food()
            elif admin_input==0:
                break
            else:
                print("please enter value input\n")
                
    elif role==2:
        res=user()
        while True:
            print("Press 1 for registartion ")
            print("Press 2 for login ")
            print("press 0 for exit  user ")
            user_input=int(input("Enter your preference "))
            if user_input==1:
                res.registration()
            elif user_input==2:
                res.login()
            elif user_input==0:
                break
            else:
                print("Please Enter correct value")
                
    elif role==3:
        sys.exit()
    else:
        print("Enter the correct value")