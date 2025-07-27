import cv2 as cv

img = cv.imread('images/cats.jpg')
#cv.imshow('Cats', img)

# 1. converting image to grayscale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

# 2. blurring an image 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT )
#cv.imshow('Blur', blur)

# 3. Edge Cascade
canny = cv.Canny(gray, 125, 175)
#cv.imshow('Canny' , canny)

# 4. Dilated 
dilated = cv.dilate(canny, (3,3), iterations = 1)
#cv.imshow('Dilated', dilated)

# 5. Eroded
Eroded = cv.erode(dilated, (3,3), iterations = 1 )
#cv.imshow('Eroded', Eroded)

# 6. Resize
resize = cv.resize(img, (500,500), interpolation= cv.INTER_AREA)
cv.imshow('Resize', resize)

# 7. Cropping 
cropping = img[50:200, 200:400]
cv.imshow('Cropping', cropping)

cv.waitKey(0)
