import cv2 as cv
#Reading Images
# img = cv.imread('images/cats_large.jpg')
# cv.imshow('cat', img)
# cv.waitKey(0)

# Reading videos
cap = cv.VideoCapture('videos/catsvideo.mp4')
while True:
    isTrue, frame = cap.read() 
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cap.release()
cap.destroyAllWindows()



