import numpy as np
import os
import pickle
from pickle import load, dump
import cv2
import imutils
import sys
import pytesseract
import pandas as pd
import time

args=sys.argv[1:]
#print(args)
image = cv2.imread(args[0])

image = imutils.resize(image, width=500,height=500)
#image=image[100:400, 100:400]

cv2.imshow("Original Image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


gray = cv2.bilateralFilter(gray, 11, 17, 17)


edged = cv2.Canny(gray, 170, 200)


(new, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
NumberPlateCnt = None 

count = 0
for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:  
            NumberPlateCnt = approx 
            break


mask = np.zeros(gray.shape,np.uint8)
new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
new_image = cv2.bitwise_and(image,image,mask=mask)
cv2.namedWindow("Final_image",cv2.WINDOW_NORMAL)
cv2.imshow("Final_image",new_image)


config = ('-l eng --oem 1 --psm 7')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

text = pytesseract.image_to_string(new_image, config=config)
print(text)

cobj=open("File.txt",'a+')
clist=[]
clist.append(text)
#print(clist)
cobj.write(clist.pop()+"\t"+args[0]+"\n")
cobj.close


raw_data = {'date': [time.asctime( time.localtime(time.time()) )], 
        'number plate': [text]}

df = pd.DataFrame(raw_data, columns = ['date', 'number plate'])
df.to_csv('data.csv')

cv2.waitKey(0)
cv2.destroyAllWindows()
exit()