# Medical store management app using oops

class Medicine:

    def __init__(self,med_id,name,price,quantity):

        self.med_id = med_id

        self.name = name

        self.price = price

        self.quantity = quantity

    def update_quantity(self,qty):

        #update medicine stock after selling


        if self.quantity >= qty:

            self.quantity -= qty

            return True

        else:

            return False

    def __str__(self):

        return f"ID: {self.med_id} , Name:{self.name} , price: {self.price} , Quantity: {self.quantity}"
    
class Customer:

        def __init__(self,cust_id,name,phone):

            self.cust_id = cust_id

            self.name = name

            self.phone = phone

            self.purchase_history = [] 

        def add_purchase(self,medicine,qty,total_price):

            self.purchase_history.append((medicine,qty,total_price))

        def display_record(self):

            if not self.purchase_history:

                print(f"{self.name} has no purchase history")    

            else:

                print(f"----Purchase History of {self.name}----") 

                for med,qty,total in self.purchase_history:

                    print(f"{qty} x {med} = ${total}")   

        def __str__(self):

            return f"Customer ID: {self.cust_id}, Name:{self.name}, Phone:{self.phone}"            


class MedicalStore:

    def __init__(self):

        self.medicines = {}

        self.customers = {}

    def add_medicines(self,medicine):

        self.medicines[medicine.med_id] = medicine

    def display_Stock(self):

        if not self.medicines:

            print("No medicines available")   

        else:

            for med in self.medicines.values():

                print(med)

    def search_medicine(self,name):

        for med in self.medicines.values():

            if med.name.lower() == name.lower():

                return med
            
        return None


    def add_customer(self,customer):

        self.customers[customer.cust_id] = customer

    def display_customer(self):

        if not self.customers:

            print("No customers registered") 

        else:

            for cust in self.customers.values():

                print(cust)

    def sell_medicine(self,cust_id,med_id,qty):

        if cust_id not in self.customers:

            print("Customer not found! Please Register first") 

            return
        

        if med_id in self.medicines:

            med = self.medicines[med_id]

            if med.update_quantity(qty):

                total = qty * med.price

                self.customers[cust_id].add_purchase(med,qty,total)

                print(f"{qty} unit(s) of {med.name} sold to {self.customers[cust_id].name}.Total Price: ${total}")

            else:

                print("Not enough stock available!")  

        else:

            print("Medicine not found!") 

def main():

    store = MedicalStore()

    while True:

        print("\n----Medical Store Management-----") 

        print("1. Add Medicine:")

        print("2. Display stock:")  

        print("3. Search Medicine:")

        print("4. Register customer:")

        print("5. Display Customers:")

        print("6. Sell medicines to customer:")

        print("7. Show customer purchase History:")

        print("8. Exit")

        choice = input("Enter your choice:")

        if choice == '1':

            med_id = input("Enter Medicine ID:")

            name = input("Enter Medicine name:")

            price = float(input("Enter the price of the medicine:"))

            qty = int(input("Enter the quantity of the medicine:"))

            medicine = Medicine(med_id,name,price,qty)

            store.add_medicines(medicine)

            print("Medicine added succesfully!")

        elif choice == '2':

            store.display_Stock()

        elif choice == '3':

            name = input("Enter Medicine name to search:")   

            med = store.search_medicine(name)

            if med:

                print("Medicine Found:", med)
                
            else:

                print("Medicine not found!")

        elif choice == '4':

            cust_id = input("Enter Customer ID:")     

            name = input("Enter customer name:")  

            phone = input("Enter Customer phone:")

            customer = Customer(cust_id,name,phone) 

            store.add_customer(customer) 

            print("Customer registered succesfully!")

        elif choice == '5':

            store.display_customer()

        elif choice == '6':

             cust_id = input("Enter Customer ID:")  

             med_id = input("Enter Medicine ID:") 

             qty = int(input("Enter the quantity of the medicine:"))

             store.sell_medicine(cust_id,med_id,qty)

        elif choice == '7':

            cust_id = input("Enter Customer ID:") 

            if cust_id in store.customers:

                store.customers[cust_id].display_record()

            else:

                print("Customer not found!")   

        elif choice == '8':

            print("Exiting...Thank you!")     

            break

        else:

            print("Invalid choice.Try again")  

if __name__ == "__main__":

    main()              














            





