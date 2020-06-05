Read-Me For Attendance System Using Facial Recognition


1. Install modules
	-opencv
		-pip3 install opencv-python
		-pip3 install opencv-contrib-python
		
	-pip3 install pillow --upgrade
	-pip3 install pickle
	-pip3 install openpyxl
	

2. Run the add_student.py to add student to database and add images to dataset
	-Type name and roll number
	-This file creates a folder with your name and clicks images which will then be added to the folder.
	-The program only clicks when we press spacebar( So that we cant get imagess that we want to be stored) and if it DETECTS A FACE(so that we do not store random photos in a given folder)
	- We have made a limit of 30 photos in the program can add more later
	- Press esc key to quit the program 
	
3. Now to train, run the face_train.py
	- This file reads all the images and the faces. Then stores labels them with the folder name.
	- The .yml file is created which is the trained model .

4. We can test the recognizer by running identify.py
	- This is an additional file

5. After training the data-set run sheet.py 
	- This program creates a sheet with the name of reporst_ise or updates it if already created
	- It also creates a column with the current date so that we mark the attendance of the current day.
	
6. Run markattend.py -i/(IMAGEPATH) to identify the people on an image and mark the attendance
	- This program identifies the faces and gives the count of how many faces were detected
	- For every present student it marks present in the sheet(1) and absent for students who are not found
	
7. Run markvideo.py this program identifies student from the webcam and marks present
 
	- This program also does the same function as the markattend but it identifies people in video.
	
	  
