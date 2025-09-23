#soln1 using time module

import time

starting_time = time.time()

print("hello world")

num1 = int(input("enter a number here:"))

num2 = int(input("enter a number here:"))

print(num1+num2)

ending_time = time.time()

elapsed_time = ending_time - starting_time

print(elapsed_time)


#soln2 using TIMEIT module

from timeit import default_timer as timer

starting_time1 = timer()

print("measure the elapsed time in python")

ending_time1 = timer()

elapsed_time1 = ending_time1 - starting_time1

print(elapsed_time1)


