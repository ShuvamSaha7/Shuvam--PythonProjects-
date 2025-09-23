import PIL

from PIL import Image

img = PIL.Image.open("C:/Users/Shuvam Saha/Pictures/coder.jpg") #location and then file name

width,height = img.size

print(f"Resolution: {width} x {height}")

