"""
main file of facial recognition
"""
import cv2
# Path to cv2:
# /Users/yingjieqiao/opencvqiao/lib/python3.7/site-packages/cv2/cv2.cpython-37m-darwin.so
import numpy as np
import pickle

face_cascade = cv2.CascadeClassifier('/Users/yingjieqiao/opencvqiao/code/cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels = {}
# The dictionary in label.pickle file is in this format: {personName: ID}
# It has to be reversed into {ID: personName}
with open("labels.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {value: key for key, value in og_labels.items()}


cap = cv2.VideoCapture(0)

while True:
    # Capture frame by frame
    ret, frame = cap.read()

    # grey scale in order for cascade to work
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # ML recognizer!!!
        id_, conf = recognizer.predict(roi_gray) # Taking label and generate confidence
        if 90 >= conf >= 50:
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)

        # save the last captured face when the code exits
        img_item = 'my-image.png'
        cv2.imwrite(img_item, roi_gray) ### NOT imgwrite() !!!!!!!!!

        ret_color = (255, 0, 0) # it is BGR, not RGB!
        stroke = 2
        width = x + w #end x coordiante
        height = y + h #end y coordinate
        cv2.rectangle(frame, (x, y), (width, height), ret_color, stroke)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
