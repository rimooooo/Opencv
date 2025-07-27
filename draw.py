import cv2 as cv
import numpy as np

blank = np.ones((500,500,3), dtype = 'uint8') #datatype of an image
cv.imshow('Blank', blank)

# 1. Paint the image as color
blank[300:400 , 400:500] = 0,255,255
cv.imshow('Color' , blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2 , blank.shape[0]), (0,0,255), thickness=cv.FILLED) #Thickness = -1 or cv.FILLED [same]
#in the above width and height is given by either values (250,500) or blank.shape[1]//2 , blank.shape[0]//2
cv.imshow('rectangle', blank)

# 3. Draw a circle 
cv.circle(blank , (blank.shape[1]//2 , blank.shape[0]//2), 100, (0,255,0), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2 , blank.shape[0]//2), (255,255,255), thickness=4)
cv.imshow('Line', blank)

# 5. Put Text 
cv.putText(blank, 'Hello myself rimjhim', (10,250), cv.FONT_HERSHEY_TRIPLEX , 1.0 , (0,255,0), 2)
cv.imshow('text', blank)

cv.waitKey(0)