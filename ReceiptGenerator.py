# Write a python program which will keep adding a stream of numbers inputted by the user.The adding stops as soon as user presses q key on the keyboard

sum = 0

while(True):
    userInput = input("Enter the item price or press q to quit:\n")

    if (userInput !='q'):

        sum += int(userInput)

        print(f"Order total so far:{sum}")

    else:
        print("Thanks for shopping with us")

        print(f"Your Bill total is {sum}")

        break    