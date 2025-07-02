import cv2
import numpy as np
from PIL import Image
import time
import os
import argparse
def choseSymbol(brightness):
    palete1 = " .`:-~=+*!?8%@#▀"

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
def createImageFromFile(imageName):
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
            print (choseSymbol(brightness_simple), end="")

            x += 1
            


        print("")
        
        y += 1
def createImage(image, block_size=1):
    pixels = image.load()
    width, height = image.size
    
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):

            total = 0
            count = 0
            
            for dy in range(block_size):
                for dx in range(block_size):
                    if y + dy < height and x + dx < width:  
                        if image.mode == 'RGBA':
                            r, g, b, a = pixels[x + dx, y + dy]
                        else:
                            r, g, b = pixels[x + dx, y + dy]
                        total += (r + g + b) // 3
                        count += 1
            
            if count > 0:
                avg_brightness = total // count
                print(choseSymbol(avg_brightness), end="")
        
        print() 
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def startVideo(video_path, blockSize):
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
            createImage(pil_image, blockSize)
            frame_count += 1
    finally:
        cap.release()
        print(f"\n end frames :  {frame_count}")

def printHelp():
    print("""
    I Wrote The Book How To Be ASCII For Dummis
    
    Flags:
    -v name.mp4         Use video image
    -b 8                BlockSizeImages
    -i Molly.png        Use imageCreator 
    -h                  Show help
    """)
def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--help", action="store_true")
    parser.add_argument("-v", "--video")
    parser.add_argument("-b", "--blockSize")
    parser.add_argument("-i", "--image")
    
    
    args = parser.parse_args()
    if args.help:
        printHelp()
        return
    if args.image:
        print(f"Image is {args.image}")
        createImageFromFile(args.image)
        return
    if args.video:
        print(f"Video is  {args.video} Block size is {args.blockSize}")
        if args.blockSize == None:
            startVideo(args.video, 1)
        else:
            startVideo(args.video, int(args.blockSize))
        return
    if args.blockSize:
        print("Use flag -h")
        return
    

if __name__=="__main__": 
    main() 