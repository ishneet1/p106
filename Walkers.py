import cv2


# Create our body classifier


# Initiate video capture for video file
cap = cv2.VideoCapture('c:/Users/saree_0rj353/Desktop/Coding/Projects/P106/walking.avi')
body_classifier=cv2.CascadeClassifier('c:/Users/saree_0rj353/Desktop/Coding/Projects/P106/haarcascade_fullbody.xml')


# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    converttogrey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=body_classifier.detectMultiScale(converttogrey)
    for (x,y,w,h) in faces:
     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    # Display the resulting frame
    cv2.imshow("Web cam", frame)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break
  
# After the loop release the cap object
cap.release()

# Destroy all the windows
cv2.destroyAllWindows()