import cv2
import pyautogui as pu

cap = cv2.VideoCapture(0)
faces_cascade=cv2.CascadeClassifier('C:\\Users\\prapul\\PycharmProjects\\opn\cascade\\data\\haarcascade_frontalface_alt2.xml')
k=0
c=0
z=0
h=0
while (True):
    ret, frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=faces_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    print(faces)
    if(len(faces)==0):
        k+=1

        if k==1:

            pu.press('space')
            c=1


        if c==1:
            continue





    k=0
    if(c==1 and len(faces)>0):
        pu.press('space')
    for (x,y,w,h) in faces:
         print(x,y,w,h)

         c=x+100
         c1=y+100
         color=(255,0,0)
         strok=2
         hight=x+h
         wid=y+w
         cv2.rectangle(frame,(x,y),(hight,wid),color,strok)






    cv2.imshow('this is', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
