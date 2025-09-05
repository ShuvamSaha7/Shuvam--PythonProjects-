with open ('C:/Users/Shuvam Saha/Documents/python work/currencyData.txt') as f:
    lines = f.readlines()

currencyDict = {}

for line in lines:
    parsed = line.strip().split("\t")

    currencyDict[parsed[0]] = parsed[1] #this line adds a key-value pair to the dictionary currencyDict where: the key is parsed[0] (example:"USD") and the value is parsed[1](example:"74.5")
                                        #'USD'='74.5'


print(currencyDict)

amount = int(input("Enter the amount:"))

print("Enter the name of currency you want to convert this amount to? Available options:\n")

[print(item) for item in currencyDict.keys()]

currency = input("please enter one of these values:\n")

print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency}")



