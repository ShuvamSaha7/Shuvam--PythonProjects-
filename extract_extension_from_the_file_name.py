#soln1 using os module

import os


file_ext = os.path.splitext("C:/Users/Shuvam Saha/Desktop/Python codes/shuvam/helloworld.py")

print(file_ext)

print(file_ext[1])


#soln2 using pathlib module

from pathlib import Path 

print(Path("C:/Users/Shuvam Saha/Desktop/Python codes/shuvam/helloworld.py").stem) #name

print(Path("C:/Users/Shuvam Saha/Desktop/Python codes/shuvam/helloworld.py").suffix) #extension