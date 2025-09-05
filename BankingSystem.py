class BankAccount:

    def __init__(self,account_number,holder_name,pin):

        self.account_number = account_number

        self.holder_name = holder_name

        self.pin = pin

        self.balance = 0

        self.transactions = [] #store history


    def authenticatePin(self,pin):

        if self.pin == pin:

            print("Authentication Successfull!")  

            return True

        else:

            print("Authentication Failed!")  

            return False




    def deposit(self,amount):

        if amount > 0:

            self.balance += amount

            self.transactions.append(f"Deposited: {amount}") 

            print(f"${amount} deposited. New Balance = ${self.balance}")  

        else:

            print("Invalid Deposit amount")  

    def withdraw(self,amount):

        if amount>0 and self.balance>=amount:

            self.balance -= amount

            self.transactions.append(f"Withdrawn: {amount}")  

            print(f"${amount} withdrawn. New Balance = ${self.balance}") 

        else:

            print("Insufficient balance or invalid amount")   

    def viewBalance(self):

        print(f"Balance for {self.holder_name}: ${self.balance}") 

    def view_transactions(self):

        print(f"Transaction History for {self.holder_name}:")   

        for t in self.transactions:

            print(" -", t) 

class CurrentAccount(BankAccount):

#Inherits Deposit and withdraw method from class BankAccount   
    pass


class SavingsAccount(BankAccount):

    def __init__(self, account_number, holder_name, pin,interest_rate):

        super().__init__(account_number, holder_name, pin)

        self.interest_rate = interest_rate

    def calculate_interest(self,months):

        if months > 0:

            years = months/12

            interest = self.balance *(1+(self.interest_rate/100))**years  

            self.balance += interest

            self.transactions.append(f"Interest Added: {interest:.2f}")  

            print(f"Interest ${interest:.2f} added.New Balance = ${self.balance:.2f}")


        else:

            print("Invalid month Input")   

# ---------- Main Banking System(client)


def main():

    accounts = {}

    while True:

        print("\n ---- Banking System Menu ----")

        print("1. Create Current Account")

        print("2. Create Savings Account")

        print("3. Deposit")

        print("4. Withdraw")

        print("5. View Balance")

        print("6. Calculate Interest (Savings only)")

        print("7. View Transactions")

        print("8. Exit")

        choice = input("Enter User choice:")

        if choice == "1":

            acc_no = input("Enter account number:")

            name = input("Enter account holder name:")

            input_pin = input("Enter pin:")

            accounts[acc_no] = CurrentAccount(acc_no,name,input_pin)

            print(f"Current Account created for {name}")

        elif choice == "2":

            acc_no = input("Enter account number:")

            name = input("Enter account holder name:")

            input_pin = input("Enter pin:")

            rate = float(input("Enter Interest Rate (%):"))

            accounts[acc_no] = SavingsAccount(acc_no,name,input_pin,rate)

            print(f"Savings Account created for {name}")

        elif choice == "3":

            acc_no = input("Enter account number:")

            input_pin = input("Enter 4 digit pin:")

            if acc_no in accounts and len(input_pin) == 4:

                amount = float(input("Enter deposit amount:"))

                accounts[acc_no].deposit(amount)

            else:

                print("Account not found")

        elif choice == "4":

            acc_no = input("Enter account number:")

            input_pin = input("Enter 4 digit pin:")

            if acc_no in accounts and len(input_pin) == 4:

                amount = float(input("Enter withdrawn amount:"))

                accounts[acc_no].withdraw(amount)

            else:

                print("Account not found")


        elif choice == "5":

            acc_no = input("Enter account number:")

            input_pin = input("Enter 4 digit pin:")

            if acc_no in accounts and len(input_pin) == 4:


                accounts[acc_no].viewBalance()


        elif choice == "6":

             acc_no = input("Enter account number:")

             input_pin = input("Enter 4 digit pin:")

             if acc_no in accounts and isinstance(accounts[acc_no],SavingsAccount) and len(input_pin) == 4:
                 
                 months = int(input("Enter  number of months:"))

                 accounts[acc_no].calculate_interest(months)

             else:

                 print("Interest available only for savings account") 

        elif choice == "7":

            acc_no = input("Enter account number:")

            input_pin = input("Enter 4 digit pin:")

            if acc_no in accounts and len(input_pin) == 4:


                accounts[acc_no].view_transactions()

            else:

                print("Account not found") 


        elif choice == "8":

            print("Exiting Banking System.GoodBye!") 

            break

        else:

            print("Invalid choice.Try again.")   


# Run the program

if __name__ == "__main__":

    main()            
















            



                







        
