import cv2 as cv 
import numpy as np

img = cv.imread ('images/cats.jpg')
#cv.imshow('Cats', img )

# Translations
def translate(img , x, y):
    transMat = np.float32([[1,0,x],[0,1,y]]) #translational matrix
    dimensions = (img.shape[1], img.shape[0]) #[1]=width, [0]=height
    return cv.warpAffine(img, transMat, dimensions)

# -x = left
# -y = up
# x = right 
# y = down    

translated = translate(img, 50, -50)
#cv.imshow('Translate', translated)

# Rotations 
def Rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2] 
    if rotPoint is None :
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) #scale =1.0
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions) 

# positive = clockwise rotation 
# negative = anti-clockwise rotation

rotated = Rotate(img , 45)   
#cv.imshow("Rotated", rotated)

Rotated_rotated = Rotate( rotated, 45)
#cv.imshow("Rotated_rotated", Rotated_rotated)
    
# Resizing    
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
## cubic gives the best result (slower but effective
## linear is fast but does not give best results as cubic
## area bhi kuchh toh hai
#cv.imshow('Resized', resized)

# Flipping 
flip = cv.flip(img , -1) #basically 0 and 1 (horizontal flip or vertical flip)
cv.imshow('Flip', flip)

# Cropping 
cropped = img[200:400 , 300:600]
cv.imshow('Cropped' , cropped)

cv.waitKey(0)