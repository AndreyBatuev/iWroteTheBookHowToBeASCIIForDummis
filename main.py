import cv2
import numpy as np
from PIL import Image
import os
def choseSymbol(brightness):
    palete2 = "  ··──││░░▒▒▓▓██" 
    selectPalete = palete2
    if brightness < 15:
        return selectPalete[0]
    elif brightness < 31:
        return selectPalete[1]
    elif brightness < 47:
        return selectPalete[2]
    elif brightness < 63:
        return selectPalete[3]
    elif brightness < 79:
        return selectPalete[4]
    elif brightness < 95:
        return selectPalete[5]
    elif brightness < 111:
        return selectPalete[6]
    elif brightness < 127:
        return selectPalete[7]
    elif brightness < 143:
        return selectPalete[8]
    elif brightness < 159:
        return selectPalete[9]
    elif brightness < 175:
        return selectPalete[10]
    elif brightness < 191:
        return selectPalete[11]
    elif brightness < 207:
        return selectPalete[12]
    elif brightness < 223:
        return selectPalete[13]
    elif brightness < 239:
        return selectPalete[14]
    elif brightness < 255:
        return selectPalete[15] 

def DEBUG_print_data_pixels(ImageName):
    image = Image.open(ImageName)  
    pixels = image.load()  
    
    width, height = image.size
    y = 0
    while y != height:
        x = 0
        while x != width:
            r, g, b, a = pixels[x, y]  
            brightness_simple = (r + g + b) // 3  
            print(f"{brightness_simple}\t",end="")
            x += 1
        print("")
        y += 1
def createImage(image):
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
            print (choseSymbol(brightness_simple), end="")

            x += 1
            


        print("")
        
        y += 1

        
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def startVideo(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Open file error")
        return
    
    frame_count = 0
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(rgb_frame)
            clearScreen() 
            createImage(pil_image)
            frame_count += 1
    finally:
        cap.release()
        print(f"\n end frames :  {frame_count}")

def main():
    startVideo("720p.mp4")
    

if __name__=="__main__": 
    main() 