
from PIL import Image

def DEBUG_print_data_pixels(ImageName):
    image = Image.open(ImageName)  
    pixels = image.load()  
    
    width, height = image.size
    y = 0
    while y != height:
        x = 0
        while x != width:
            r, g, b, a = pixels[x, y]  
            brightness_simple = (r + g + b) // 3  # Среднее
            print(f"{brightness_simple}\t",end="")
            x += 1
        print("")
        y += 1
def createImage(imageName):
    image = Image.open(imageName)  
    pixels = image.load()
    width, height = image.size
    y = 0
    while y != height:
        x = 0
        while x != width:
            if image.mode == 'RGBA':
                r, g, b, a = pixels[x, y]
            else:
                r, g, b = pixels[x, y]

            
            brightness_simple = (r + g + b) // 3 
            if brightness_simple == 0:
                print(" ", end="")
            elif brightness_simple == 13:
                print("|", end="")
            elif brightness_simple == 160:
                print("Y", end="")

            x += 1
            


        print("")
        
        y += 1


def main():
    DEBUG_print_data_pixels("Molly.png")
    createImage("Molly.png")
if __name__=="__main__": 
    main() 