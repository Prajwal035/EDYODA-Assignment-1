import json

class admin:
    def __init__(self):
        self.food={}
    
    def add_food_items(self):
        self.name=input("Enter the food name ")
        self.quantity=input("Enter the quantity ")
        self.prize=int(input("Enter the prize "))
        self.discount=int(input("Enter the discount "))
        self.stock=int(input("Enter the stock "))
        self.items={"name":self.name,"quantity":self.quantity,"prize":self.prize,"discount":self.discount,"Stock":self.stock}
        print(self.items)
        self.food_id=len(self.food)+1
        self.food[self.food_id]=self.items
        with open("food_items.json","w") as f:
            json.dump(self.food,f)
        print("Food items added successfully")
        
    def remove_food(self):
        for k,v in self.food.items():
            print("Food ID is ",k," Food items are ",v)
        del self.food[int(input("Enter the Food ID to be deleted "))]
        with open("food_items.json","w") as f:
            json.dump(self.food,f)
        print("Item deleted successfully")
    
    def view_food(self):
        for k,v in self.food.items():
            print("Food ID is ",k," Food items are ",v)
            
    def edit_food_items(self):
        f_id=int(input("Enter the food ID to be edited"))
        for i in self.food[f_id]:
            self.food[f_id][i]=input(f"Enter the {i} value to be updated")
        with open("food_items.json","w") as f:
            json.dump(self.food,f)
        print("Food details has been updated ")

            
        
    
    