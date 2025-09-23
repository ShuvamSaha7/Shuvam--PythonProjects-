# program to safely create a nested directory

import pathlib

from pathlib import Path

Path("C:/Users/Shuvam Saha/Documents/Custom Office Templates/new_dict/demo_dict/hello_shuvam").mkdir(parents = True,exist_ok = True)

# In Python using pathlib module, the mkdir() metod accepts two commonly used parameters

#path().mkdir(parents = False, exist_ok=False)

# parents if True it creates parent directories as needed

#exist_ok if True it won't raise an error if the folder already exists



