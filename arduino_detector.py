import cv2
import os


def empty(a):
    pass


################################################################
path = r'C:\Users\E17538\OneDrive - Uniper SE\Desktop\DailyActivities\FAD\ACV_S6__HW\OpenCV-Python-Tutorials-and-Projects\HW\classifier/arduino_cascade.xml'  # PATH OF THE CASCADE
cameraNo = 0                       # CAMERA NUMBER
objectName = 'Arduino'       # OBJECT NAME TO DISPLAY
frameWidth= 640                     # DISPLAY WIDTH
frameHeight = 480                  # DISPLAY HEIGHT
color= (255,0,255)
#################################################################

img_path = r'C:\Users\E17538\OneDrive - Uniper SE\Desktop\DailyActivities\FAD\ACV_S6__HW\OpenCV-Python-Tutorials-and-Projects\HW'
img_name = 'arduino_test3.jpg'
img_path = os.path.join(img_path, img_name)
img = cv2.imread(img_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# CREATE TRACKBAR
# cv2.namedWindow("Result")
# cv2.resizeWindow("Result",frameWidth,frameHeight+100)
# cv2.createTrackbar("Scale","Result",400,1000,empty)
# cv2.createTrackbar("Neig","Result",8,50,empty)
# cv2.createTrackbar("Min Area","Result",0,100000,empty)
# cv2.createTrackbar("Brightness","Result",180,255,empty)

# LOAD THE CLASSIFIERS DOWNLOADED
cascade = cv2.CascadeClassifier(path)

# scaleVal = 1 + (cv2.getTrackbarPos("Scale", "Result") / 1000)
# neig = cv2.getTrackbarPos("Neig", "Result")


scaleVal = 100
neig = 2
minArea = 0


objects = cascade.detectMultiScale(img_gray, scaleVal, neig)


# DISPLAY THE DETECTED OBJECTS
for (x, y, w, h) in objects:
    area = w * h
    minArea = cv2.getTrackbarPos("Min Area", "Result")
    if area > minArea:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
        cv2.putText(img, objectName, (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
        roi_color = img[y:y + h, x:x + w]

cv2.imshow("Result", img)

cv2.waitKey(0)





