import os
import cv2
import numpy as np
from PIL import Image
import pickle
#Face cascade used for face detector
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
#This is to used for Face Recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
#The next two statements is to get the path to images
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_dir=os.path.join(BASE_DIR,"dataset")

current_id = 0
label_ids= {}
y_labels = []
x_train = []
#this is to search for the files in the directory
for root, dirs, files in os.walk(img_dir):
	c=0
	#this is to searc for the image files
	for file in files:
		if file.endswith("png")  or file.endswith("jpeg") or file.endswith("jpg"):
			#This is to create the labels
			path = os.path.join(root,file)
			label =os.path.basename(root).replace(" ", "-").lower()
			
			if not label in label_ids:
				label_ids[label] = current_id
				current_id += 1
			id_=label_ids[label]
			#print (label_ids)
			##y_labels.append(label)
			##x_train.append(path)
			#This converts the image into grayscale and resizes it
			pil_image = Image.open(path).convert("L")
			size =(550,550)
			final_image =pil_image.resize(size,Image.ANTIALIAS)
			#this reads the final image
			image_array =np.array(final_image,"uint8")
			##print(image_array)
			#Ths detects the face in image
			faces =face_cascade.detectMultiScale(image_array, scaleFactor= 1.1,minNeighbors= 3)
			#For the face in image
			for(x,y,w,h) in faces:
				#We take the region of interest i.e, The Face
				roi =image_array[y:y+h , x:x+h]
				#This appends the face with id
				x_train.append(roi)
				y_labels.append(id_)
				c=c+1
		print(label,c)
			
##print(y_labels)
##print(x_train)
#Now we use pickle to serialize labels
with open("labels.pickle","wb") as f:
	pickle.dump(label_ids,f)
#We can train the model and save it ad trainner.yml
recognizer.train(x_train,np.array(y_labels))
recognizer.save("trainner.yml")
