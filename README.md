# Face-Recognition
***
## Short description of the project.
In this project the face recognition model is built with the help of face_recognition module from python.
openCV is used inorder to capture the frames from the video stream and process it against face recognition.

## Process of bulding the Facial recognition system.
The process for building facial recognition system is : 
1. Load the images from the train directories using the load_images funtion of face_recognition module.
2. Encode the faces using the face_encoding function.
3. Store the encodings and corresponding names of the images in the train directories.
4. The values for the model and tolerence are set accordingly.

## Testing with live camera.
1. Read the frames using the cv2.videoCapture().
2. Trace the locations of all the faces in the captured frame.
3. Encode the faces in the found locations.
4. Comapre the encodings with the encodings of the images in the train directories.
5. If a match is found the name is displayed on the rectangle drawn around the face found in the captured frame.
6. Else, soory is printed on the rectangle.
7. The VideoCapture ends on pressing 'q'.
