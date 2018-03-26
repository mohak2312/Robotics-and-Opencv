import cv2
import numpy as np

def face_recognizer(im):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('Face recogization/face_recognizer.xml')
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        print(Id)
        f=open('./info.txt')
        lines = f.read().splitlines()
        name=lines[Id-1].split("_")
        print(name)
        cv2.putText(im,str(name[0]),(x,y-3),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA)     
    return name if name != None else "None"
