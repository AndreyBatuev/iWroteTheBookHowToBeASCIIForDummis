
from PIL import Image


image = Image.open("Molly.png")  
pixels = image.load()
width, height = image.size
x = 0
while x != width:
    y = 0
    while y != height:
        r, g, b, a = pixels[x, y] 
        brightness_simple = (r + g + b) // 3 
        if brightness_simple == 0:
            print(" ", end="")
        elif brightness_simple == 13:
            print("|", end="")
        elif brightness_simple == 160:
            print("Y", end="")

        y += 1
        


    print("")
       
    x += 1
    