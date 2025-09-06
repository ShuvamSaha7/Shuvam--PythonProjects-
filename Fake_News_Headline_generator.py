# We will create fake + funny headline

# EXample - "Shahrukh Khan spotted riding a Buffalo cart near India Gate"

# Here we will see use of lists , random module , print() , input() , while loop(until user says no) , fstring or string concatenation

# Step -1 -> import the random module

# step -2 -> create lists of subjects,actions,and places/objects

# step -3 -> use random.choice() to pick one word from each list

# step -4-> combine the words into a headline using fstring

# step -5-> print the headline to the user

# step -6-> ask the user if they want another headline

# step -7-> If yes repeat ; if no stop the program


import random 

subjects = ["Shahrukh Khan", "Cristiano Ronaldo", "Virat Kohli" , "Nirmala Sitharaman", "Dwayne Johnson", "AI Robot from IIT", "Lady Gaga" , "Shuvam Saha", "T-Series", "Batman",  "Tom Cruise" ,"Will Smith", "Elon Musk", "Mark zuckerberg", "Stepen Hawking"]

actions = ["invade", "ban", "discover", "accidentally create", "sue", "blame", "hack", "confess to", "clone", "declare war on", "steal", "leak", "approve", "predict", "cancel", "expose", "launch", "arrest", "worship", "resurrect", "buy", "sell", "endorse", "protest against", "replace", "burn", "teleport to", "hypnotize", "control", "elect", "reject", "swallow", "rename", "misplace", "decode", "weaponize", "smuggle", "cry over", "eat", "dance on", "paint", "build a statue of", "time travel to", "rent", "start a petition against", "banish", "summon", "marry", "divorce", "leak secrets about", "mistake for", "interrogate", "cancel plans with", "brainwash", "follow", "spy on"]



places_or_things =  [ "a flying dosa" , "invisible goat" , "talking dustbin" , "haunted AC remote" , "alien pani puri vendor", "emotional ATM machine", "AI powered mosquito", "KOlkata metro ghost coach", "robot that sings Bhojpuri" , "solar powered kurkure packet", "underwater Whatsapp group","an AI powered broom", "a spicy maggi tornado", "a math book that gives relation advice", "a bluetooth enabled chappal", "a potato that runs on petrol"]




while True:

    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS : {subject} {action} {place_or_thing}"


    print("\n"+ headline)

    user_choice = input("Do you want another headline? (yes/no)").strip().lower()

    if user_choice == "no":
        break


print("Thanks for using the Fake News Headline Generator Program.Have a fun day")    





