import json
import sys
from admin import *
class user:
    def __init__(self):
        self.users={}
        self.orders={}
        
    def registration(self):
        self.full_name=input("Enter the full name ")
        self.phone_number=int(input("Enter the Phone number "))
        self.email=input("Enter yor email ID ")
        self.address=input("Enter your address ")
        self.password=input("Enter yor password ")
        self.user_info={"fullname":self.full_name,"phonenumber":self.phone_number,"email":self.email,"address":self.address,"password":self.password}
        self.u_id=len(self.users)+1
        self.users[str(self.u_id)]=self.user_info
        with open("user_registration.json","w") as f:
            json.dump(self.users,f)
        print("User Registration Successful..")
        
    def place_order(self):
        with open("food_items.json","r") as f:
            ite=json.load(f)
        for k,v in ite.items():
            print(v["name"] + "("+v["quantity"]+")" + "[INR"+ str(v["prize"])+"]")    
        food_n=eval(input("Enter the list of fod items to be added "))
        print(str(food_n))
        ords=dict()
        for i in food_n:
            for j  in ite.keys():
                if i==int(j):
                    ords[j]=ite[j]
        with open("user_orders.json","w") as d: 
            json.dump(ords,d)
            
    def edit_order(self):
        print("order history")
        with open("user_orders.json","r") as e:
            O_H=json.load(e)
            print(O_H)
        element=input("Enter the number for deleting the order number else enter 0 to return")
        if int(element)==0:
            return
        else:
            del O_H[element]
            with open("user_orders.json","w") as d: 
                json.dump(O_H,d)
        
    def login(self):
        Emailid=input("Enter yor email ID ")
        passwordid=input("Enter your password ")
        with open("user_registration.json","r") as f:
            data=json.load(f)
        for k,v in data.items():
            if v["email"]==Emailid and v["password"]==passwordid:
                print('Login Successful')
                while True:
                    print("Press 1 for Place New Order ")
                    print("Press 2 for edit Order History ")
                    print("Press 3 for Update Profile ") 
                    print("Press 0 for log out")
                    pref=int(input("Enter the preferences "))
                    if pref==1:
                        self.place_order()
                    elif pref==2:
                        self.edit_order()
                    elif pref==3:
                        for i in data[k]:
                            print(data[k])
                            self.users[k][i]=input(f"Enter the {i} value to be updated ")
                        with open("user_registration.json","w") as f:
                            json.dump(self.users,f)
                        print("userr details has been updated ")
                    elif pref==0:
                        break  
                    else:
                        print("please enter correct input")
            else:
                sys.exit()
                                                   
        print("Login Unsuccessful ")
        
        

            
        
     