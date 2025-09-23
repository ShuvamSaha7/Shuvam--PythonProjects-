import random

def penalty_shootout():

    print("Welcome to the Penalty Shootout Game!")

    user_club = input("Enter the club you support:")

    computer_club = input("Enter the club computer support:")

    print(f"{user_club} will take 5 penalty shots against the {computer_club}.")

    print("Let's see who scores the most goals!\n")

    user_score = 0

    computer_score = 0

    for i in range(1,6):

        print(f"Round {i}:")

        user_shoot = input("Choose a direction to shoot(left,center,right):").lower()

        computer_save = random.choice(["left","center","right"])

        if user_shoot == computer_save:

            print("Oh no! The goalkeeper saved your shot!")

        else:

            print("Goal! You scored!")

            user_score+=1



        computer_shoot = random.choice(["left","center","right"])

        user_save = input("Choose a direction to dive (left,center,right):").lower()


        if computer_shoot == user_save:

            print("Great save! you stopped the computer's shot!")

        else:

            print("The computer scored!")   

            computer_score+=1

        print(f"Score after Round {i} : {user_club} {user_score} - {computer_score} {computer_club}") 


    print("Final Score:")  

    print(f"{user_club} : {user_score}")

    print(f"{computer_club} : {computer_score}") 

    if user_score > computer_score:

        print(f"Congratulations! {user_club} won the penalty shootout!")

    elif computer_score > user_score:

        print(f"Better luck next time! {computer_club} won the penalty shootout!") 

    else:

        print("It's a draw! what a thrilling match!")


penalty_shootout()










