import cv2                                                                       
import numpy as np                                                             
import sqlite3
import os                                                                       
import time
#Face cascade used for face detector
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
#Insert or Update Function is used to insert or update a record in SQL Dtabase
def insertOrUpdate(Id, Name, roll) :                                          
#This connects to Sqlite database 
    connect = sqlite3.connect("Face_DataBase") 
# This selects students from students based on their id                            
    cmd = "SELECT * FROM Students WHERE ID = " + Id    
# This executes the query and returns the results                  
    cursor = connect.execute(cmd)
    
    isRecordExist = 0
    personId="user"+Id
# This to traverse through the results to check if there exists 
    for row in cursor:                                                          
        isRecordExist = 1
# If the records exists then update the recird
    if isRecordExist == 1:                                                      
        connect.execute("UPDATE Students SET Name = ? WHERE ID = ?",(Name, Id))
        connect.execute("UPDATE Students SET Roll = ? WHERE ID = ?",(roll, Id))
# If it did not exist then insert the record into the database        
    else:                                               
    	connect.execute("INSERT INTO Students(ID, Name, Roll,personId) VALUES(?, ?, ?, ?)", (Id, Name, roll,personId))
# Commit saves the changes in the sql database and then closes the connection to the database
    connect.commit()                                                            
    connect.close()                                                            



#This is where the code starts
#takes input from the user
name = input("Enter Student name : ")
roll = input("Enter Student Roll Number : ")
Id = roll[-2:]
#calls the function and sends the parameters
insertOrUpdate(Id, name, roll)                                                  

#This is to create a new folder path so that we can add images in that
folderName = "user" + Id                                                        
folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dataset/"+folderName)
#If the folder path does not exist this creates
if not os.path.exists(folderPath):
    os.makedirs(folderPath)
# Cam is assigned with the VideoCapture 
cam=cv2.VideoCapture(0)
#image counter
img_counter = 0

while True:
	# This returns if the frame is read or not.It Capture frame-by-frame
	ret, frame=cam.read()
	#This converts the image into gray
	gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#This is to detect the face
	faces =face_cascade.detectMultiScale(gray, scaleFactor= 1.05,minNeighbors= 5)
	#It is used so that the system can take input from your keyboard to break or to perform an operation
	k=cv2.waitKey(1)
	#imshow displays the Frame 
	cv2.imshow('frame',frame)
	#This for loop gives us each face in the frame
	for (x, y, w, h) in faces:
		#if the image counter it breaks
		if img_counter >30:
			break
		#if you press Esc key it breaks
		elif k%256 ==27:
			print("Escaped hit,closing...")
			break
		#If you press spacebar then the image is clicked	
		elif k%256 == 32:
			#Image is written in the specified directory
			img_name="dataset/user"+Id+"/"+"{}.png".format(img_counter)
			print("{} written!".format(img_name))
			img_counter += 1
			cv2.imwrite(img_name,frame) 
			#time.sleep makes the system wait
			time.sleep(2)
			cv2.imshow('frame',frame)
			color = (255 ,0, 0)
			stroke=2
			end_cord_x= x+w
			end_cord_y= y+h
			cv2.rectangle(frame, (x,y), (end_cord_x,end_cord_y),color ,stroke)
	if k%256 ==27:
			print("Escaped hit,closing...")
			break
		
	
#This is to close all the resources we used
cam.release()
cv2.destroyAllWindows()
sampleNum = 0
