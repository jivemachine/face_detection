# import open cv
import cv2
# initializing our model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# pulling our image
img = cv2.imread("test_image.jpeg")
# converting our image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# detecting faces
faces = face_cascade.detectMultiScale(gray, 1.5, 4)
# for loop to draw a rectangle around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# shows image 
cv2.imshow('img', img)
# keypress will close program
cv2.waitKey()