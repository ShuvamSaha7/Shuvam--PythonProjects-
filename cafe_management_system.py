# Define the menu of the cafe
# Python Cafe 
menu = {
       "Pizza":115  , 
       "Pasta":130  , 
       "Burger":110 ,
       "Salad" :90  ,
       "Coffee":120 ,
}

#Greet

print("Welcome to our Python Cafe")

print("Check out our menulist first:")

print(" Pizza: RS 115\n Pasta: RS 130\n Burger: RS 110\n Salad: RS 90\n Coffee: RS 120")

order_total = 0

order_1 = input("Enter the name of item you want to order:")

if order_1 in menu:
        
        order_total += menu[order_1]

        print(f"your item {order_1} has been added to your order")
    
else:
        
        print(f"Ordered item {order_1} is not available yet")

       
       
while True:
      another_order = input("Do you want to add another item? (Yes/No):")

      if another_order == "Yes":

          order_2 = input("Enter the name of item you want to order after previous:")

          if order_2  in menu:

            order_total += menu[order_2]

            print(f"Item {order_2} has been added to order")

      else:   
             break

print("Thank you for using our program") 

print(f"The total bill you have to pay is RS.{order_total}")        
          










