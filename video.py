import os
import numpy as np
import cv2
import face_recognition


tolerance=0.6
frame_thickness=2
font_thickness=3
model="hog"

known_images_dir=r"C:\Data sets\face_recognition\known"
#unknown_images_dir=r"C:\Data sets\face_recognition\unknown"

video=cv2.VideoCapture(0)

known_faces=[]
known_names=[]

for names in os.listdir(known_images_dir):
    image=face_recognition.load_image_file(os.path.join(known_images_dir,names))
    encoding=face_recognition.face_encodings(image)[0]
    known_faces.append(encoding)
    known_names.append(names.split('(')[0].split('.')[0])

while(True):
  #print(names)
  #image=face_recognition.load_image_file(os.path.join(unknown_images_dir,names))
  ret,image=video.read()
  locations=face_recognition.face_locations(image,model=model)
  encodings=face_recognition.face_encodings(image,locations)
  #image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

  for face_encoding,face_location in zip(encodings,locations):
    results=face_recognition.compare_faces(known_faces,face_encoding,tolerance)
    match=None
    if True in results:
      match=known_names[results.index(True)]
      print("match found "+match)
      top_left=(face_location[3]-15,face_location[0]-15)
      bottom_right=(face_location[1]+15,face_location[2]+15)
      color=[0,255,0]
      cv2.rectangle(image,top_left,bottom_right,color,frame_thickness)
      
      top_left=(face_location[3]-15,face_location[2])
      bottom_right=(face_location[1]+15,face_location[2]+22)
      cv2.rectangle(image,top_left,bottom_right,color,cv2.FILLED)

      cv2.putText(image,match,(face_location[3],face_location[2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(100,50,50),1)
    else:
        top_left=(face_location[3]-15,face_location[0]-15)
        bottom_right=(face_location[1]+15,face_location[2]+15)
        color=[255,0,0]
        cv2.rectangle(image,top_left,bottom_right,color,frame_thickness)
      
        top_left=(face_location[3]-15,face_location[2])
        bottom_right=(face_location[1]+15,face_location[2]+22)
        cv2.rectangle(image,top_left,bottom_right,color,cv2.FILLED)

        cv2.putText(image,"sorry",(face_location[3],face_location[2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(100,50,50),1)
  cv2.namedWindow ('video', cv2.WINDOW_NORMAL)
  cv2.setWindowProperty ('video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
  cv2.imshow("video",image)
  if cv2.waitKey(1) & 0xFF==ord("q"):
      break

video.release()
cv2.destroyAllWindows()
  #cv2.waitKey(10000)