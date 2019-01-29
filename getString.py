import cv2
import numpy as np
from PIL import Image
import pytesseract
import os
from google import google

path = os.getcwd() + '/'
print("This is the working directory   " + path)
name = raw_input("\n\nEnter the name of the image \t")
#print("\n\n name is of type \t" + type(name))
#print("\n\n path2 is of type \t" + type(path2))
def getString(img_path):
    #read
    img = cv2.imread(img_path)
    #convert to gray
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #create kernel
    kernel = np.ones((1,1),np.uint8)
    #applying dilation and erosion to remove noise
    img = cv2.dilate(img,kernel,iterations = 1)
    img = cv2.erode(img,kernel,iterations = 1)

    #save intermediate image
    img = cv2.imwrite(path + "int.png", img)
    path1 = path + "int.png"
    
    #the string we want
    resultString = pytesseract.image_to_string(Image.open(path1))

    return resultString

def gSearch(queryString):
    searchResults = google.search(queryString)
    return searchResults
print('\n\n-----Recognizing Start------\n\n')
path1 = path + name + ".png"
print ('\n\n' + path1 + "\n\n")
resultStr = getString(path1)

print 'The result of the recognition is ' + resultStr

sResult = gSearch(resultStr)




print('\n\n------Done------')
