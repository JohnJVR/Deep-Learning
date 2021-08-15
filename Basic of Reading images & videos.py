# cv2 for Computer Vision

import cv2

# Reading Images

img = cv2.imread("E:\Edureka\computer vision\Day_1_OpenCV/copy_dog.jpg")
cv2.imshow("output",img)
cv2.waitKey(0)
 
# Importing Videos

vdo = cv2.VideoCapture("E:\Edureka\computer vision\Day_1_OpenCV/crowd.mp4")

while True:
    success, img1 = vdo.read() # capturing image and saves it as image varianle
    cv2.imshow("video",img1)
 # Wait for the delay and wait for the user to enter 'q' to break the loop   
    if cv2.waitKey(1000) & 0xFF ==ord('q'):
        break

# Reading Webcam

cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100) # Increase of the brighness in the live video feed

while True:
    success, img1 = cap.read() # capturing image and saves it as image varianle
    cv2.imshow("video",img1)
 # Wait for the delay and wait for the user to enter 'q' to break the loop   
    if cv2.waitKey(1000) & 0xFF ==ord('q'):
        break

