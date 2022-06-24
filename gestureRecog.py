import cv2 # import the cv pacakge
import sklearn


cap = cv2.VideoCapture(0) # video capture source camera (from webcam; program should automatically use the primary camera) 

while(True): # take a single frame, and display it while(True)
    ret,frame = cap.read() # return a single frame (an array of rgb values) in the variable `frame`
    cv2.imshow('img1',frame) #display the captured image
    cv2.imwrite('C:/Users/baska/Downloads/computer_vision_tutorial/image.png',frame) # save the image as "image.png" in a selected folder
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        cv2.destroyAllWindows() # close the display
        break # exit the loop

cap.release() # release camera device resource