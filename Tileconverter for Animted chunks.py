from PIL import Image
import tkinter as tk
import time as t
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
tk.Tk().withdraw() 
# Left heißt abstand von der linken kante
#Top heißt abstand von der oberen kannte
#Right is grenze wie viele pixel zwischen left und crop ende sind
#Lower genauso wie right
print('Converted made by Argonien')
print('This programm converts 24x24 tiles into 8x8 tile frame rows')
print('For this programm to work, you need to order your frames in the following way:')
print('□□□□□□□□□□□□□□□□□□')
print('Meaning from frame 1 to the last frame from left to right with NO pixels between the frames')
print('A selector windows will open shortly')
t.sleep(2)
left = 0
right = 8
top = 0
lower = 8
index = 0
imagecounter = 1
print('Select input file')
inputimage = askopenfilename()
print('Select output path')
output_path = askdirectory()
#print(output_path)
print('Please enter the number of frames')
framenumber = int(input())
print('Creating individual frames')


for i in range(framenumber*9):
    img = Image.open(f"{inputimage}")
    box = (left,top,right,lower)
    imgOut = img.crop(box)
    if (index < framenumber*3):
        if (index < framenumber):
            imgOut = imgOut.save(f"{output_path}\\"+ str(imagecounter) +".png")
            index += 1
            left += 24
            right += 24
            imagecounter += 1
            if (index == framenumber):
                left = 8
                right = 16
                #imagecounter = 0

        elif (index < framenumber*2):
            if (index <= framenumber*2):
                imgOut = imgOut.save(f"{output_path}\\"+ str(imagecounter) +".png")
                index += 1
                left += 24
                right += 24
                imagecounter += 1
                if (index == framenumber*2):
                    left = 16
                    right = 24
                    #imagecounter = 0

        elif (index < framenumber*3):
            if (index <= framenumber*3):
                imgOut = imgOut.save(f"{output_path}\\"+ str(imagecounter) +".png")
                index += 1
                left += 24
                right += 24
                imagecounter += 1
                if (index == framenumber*3):
                    left = 0
                    right = 8
                    top = 8
                    lower = 16
                    #imagecounter = 0

    elif(framenumber*3 <= index < framenumber*6):#framenumber*3 < index < framenumbver*6
        if (index < framenumber*4):
            if (index < framenumber*4):
                imgOut = imgOut.save(f"{output_path}\\"+ str(imagecounter) +".png")
                index += 1
                left += 24
                right += 24
                imagecounter += 1
                if (index == framenumber*4):
                    left = 8
                    right = 16
                    #imagecounter = 0

        elif (index < framenumber*5):
            if (index <= framenumber*5):
                imgOut = imgOut.save(f"{output_path}\\"+ str(imagecounter) +".png")
                index += 1
                left += 24
                right += 24
                imagecounter += 1
                if (index == framenumber*5):
                    left = 16
                    right = 24
                    #imagecounter = 0

        elif (index < framenumber*6):
            if (index <= framenumber*6):
                imgOut = imgOut.save(f"{output_path}\\"+ str(imagecounter) +".png")
                index += 1
                left += 24
                right += 24
                imagecounter += 1
                if (index == framenumber*6):
                    left = 0
                    right = 8
                    top = 16
                    lower = 24
                    #imagecounter = 0

    elif(framenumber*6 <= index < framenumber*9):
        if (index < framenumber*7):
            if (index < framenumber*7):
                imgOut = imgOut.save(f"{output_path}\\"+ str(imagecounter) +".png")
                index += 1
                left += 24
                right += 24
                imagecounter += 1
                if (index == framenumber*7):
                    left = 8
                    right = 16
                    #imagecounter = 0

        elif (index < framenumber*8):
            if (index <= framenumber*8):
                imgOut = imgOut.save(f"{output_path}\\"+ str(imagecounter) +".png")
                index += 1
                left += 24
                right += 24
                imagecounter += 1
                if (index == framenumber*8):
                    left = 16
                    right = 24
                    #imagecounter = 0

        elif (index < framenumber*9):
            if (index <= framenumber*9):
                imgOut = imgOut.save(f"{output_path}\\"+ str(imagecounter) +".png")
                index += 1
                left += 24
                right += 24
                imagecounter += 1
                if (index == framenumber*9):
                    left = 0
                    right = 8
                    top = 16
                    lower = 24
                    #imagecounter = 0
#Info: die ersten drei wiederhohlungen der framrate sind die gesammte oberer reihe, jeder weiter drei eine jeweilige reihe, bis 3 reihen
print('Done, created',int(index),'images')
print('Creating Importfile')

imgw = framenumber*8    #Image width
imgh = 72   #Image height
imagecounter = 1
imgposx = 0
imgposy = 0
importfile = Image.new(mode="RGB", size=(imgw,imgh))
framecount = 1
secondrange = framenumber

path = output_path
print('Full output path')
print(f"{output_path}\\"+str(framecount)+".png")

for i in range(9):
    for i in range(secondrange):
        imgframe = Image.open(f"{output_path}\\"+str(framecount)+".png")
        importfile.paste(imgframe,(imgposx,imgposy))
        imgposx += 8
        framecount +=1
    imgposy += 8
    imgposx = 0
    #secondrange += framenumber

importfile.save(f"{output_path}\\finalimport.png")
print('Done. File can be found in the output folder as finalimport.png')
t.sleep(60)