# import open cv
import cv2
# initializing our model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

class DetectFace(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    
    def __del__(self):
        self.cap.release()
    
    def get_frame(self):
        # grab single frame of video
        ret, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (250, 0, 0), 2)
        
        cv2.imshow('frame', frame)
        
        ret, jpeg = cv2.imencode('.jpg', frame)
        return (jpeg.tobytes())