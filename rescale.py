import cv2 as cv 

#reading image
img = cv.imread('images/cats1.jpg')
cv.imshow('Cats', img)

#defining a rescaling function , and then using this function
def rescaleFrame (frame , scale= 0.75): #scaling to 75%
    #images, videos and live videos 
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0]* scale)

    dimensions = (width , height)

    return cv.resize(frame , dimensions , interpolation= cv.INTER_AREA)

resized_img = rescaleFrame(img)
cv.imshow('Image', resized_img)

def changeRes (width , height):
    # live videos 
    cap.set(3, width)
    cap.set(4, height)

#reading video
cap = cv.VideoCapture('videos/catsvideo.mp4')
while True:
    isTrue, frame = cap.read() 
    frame_resized = rescaleFrame(frame , scale = 0.2) #scaling to 20%
    cv.imshow('Video', frame)
    cv.imshow('Video_Resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cap.release()
cap.destroyAllWindows()