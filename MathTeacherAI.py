# importing require libraries

import random

import sympy #for algebric equation

#creating functions to generate math questions with solutions

def generate_math_problems():

    #adding math topic

    topic = random.choice(['arithmetic', 'algebra', 'geometry'])

    if topic == "arithmetic":

        num1 = random.randint(1,28)

        num2 = random.randint(1,28)

        operator = random.choice(['+', '-', '*', '/'])

        problem = f'What is {num1} {operator} {num2} ?'

        solution = eval(str(num1)+ operator +str(num2)) #evaluate the expression to get the answer

     

    elif topic == "algebra":

        a ,b ,x = sympy.symbols("a b c")  

        a_val = random.randint(1,10)

        b_val = random.randint(1,10)

        equation = sympy.Eq(a*x + b, random.randint(1,20))

        problem = f"Slove for x: {a_val}x + {b_val} = {equation.rhs}"

        solution = sympy.solve(equation,x)
    
    


    elif topic == "geometry":

        shapes = ["circle", "triangle", "rectangle", "square"] 

        shape = random.choice(shapes)

        if shape == "circle":

            radius = random.randint(1,10)

            problem = f"What is the area of the circle with radius {radius}?"

            solution = round(3.14159 * radius**2 , 2)


        elif shape == "traingle" :

            base = random.randint(1,10) 

            height = random.randint(1,10)

            problem = f"What is the area of the triangle with base {base} and height {height}?"

            solution = 0.5 * base * height

        elif shape == "rectangle" :

            length = random.randint(1,10) 

            width = random.randint(1,10)

            problem = f"What is the area of a rectangle with length {length} and width {width}?"

            solution = length * width

        else:#square

            side = random.randint(1,10)

            problem = f"what is the area of a square with side length {side}?"  

            solution = side**2


    return problem,solution #both values are returned as a tuple
    


while True:

    problem , solution = generate_math_problems() #the returned tuple is unpacked into two varaibles

    print(problem)

    print("Solution Related to the problem:",solution)

    user_input = input("Press enter for the next problem or type 'exit' to quit:")

    if user_input.lower() == "exit":

        print("Exiting Math Teacher Program.GoodBye!")

        break

                








        
