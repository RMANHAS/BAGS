import cv2
import glob


all_images = glob.glob("*.jpeg")


detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

for image in all_images:
    img = cv2.imread(image)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face=detect.detectMultiScale(grey,1.5,5)

for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("multipeface detection",img)

cv2.waitKey(2000)








