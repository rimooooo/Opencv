import cv2 as cv 
import numpy as np

img = cv.imread ('images/cats.jpg')
#cv.imshow('Cats', img )

# Translations
def translate(img , x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 50, -50)
cv.imshow('Translate', translated)

# -x = left
# -y = up
# x = right 
# y = down    

# Rotations 
def Rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]
    

cv.waitKey(0)