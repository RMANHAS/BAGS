import cv2

detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imp_img = cv2.VideoCapture("boy.jpeg")
res, img = imp_img.read()

grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face = detect.detectMultiScale(grey,1.5,5)

for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)


cv2.imshow("face detection",img)

cv2.waitKey(4560)
imp_img.release()






