'''
Get the training pictures, turn pics into arrays
'''
import cv2
import os
from PIL import Image
import numpy as np
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
### It has to be upper case: BASE_DIR!!!!!!
image_dir = os.path.join(BASE_DIR, "images")

face_cascade = cv2.CascadeClassifier('/Users/yingjieqiao/opencvqiao/code/cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0 # To tag each person with a unique ID
label_ids = {} # {personName: ID}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
            if label in label_ids:
                pass
            else:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label] # To tag each person with a unique ID

            pil_image = Image.open(path).convert("L") # convert() method turns it into gray
            ################    VERY IMPORTANT      ################
            #### Take the value of every pixel: image --> array ####
            image_array = np.array(pil_image, "uint8")
            '''
            size = (550, 550)
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(final_image, "uint8")
            '''

            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5) #same as face_rec.py
            for (x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

with open("labels.pickle", "wb") as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainer.yml")