import cv2

video = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
no = 1

while True:
    success,img = video.read()
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayImg,1.1,4)
    keyPressed = cv2.waitKey(1)

    for x,y,w,h in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),0)
        smiles = smileCascade.detectMultiScale(grayImg,1.8,15)
        for x,y,w,h in smiles:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),0)
            path=r'C:\Users\Vedha Vikash\Pictures\smile\image'+str(no)+'.jpg'
            cv2.imwrite(path,img)
            print("Image captured ")
            print("Your camera is waiting for your smile :)")
            no= no + 1
            
    cv2.imshow('SAY CHEESE',img)
    if(keyPressed & 0xFF==ord('q')):
        break

video.release()                                  
cv2.destroyAllWindows()