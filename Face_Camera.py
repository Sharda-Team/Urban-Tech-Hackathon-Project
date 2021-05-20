import cv2

Cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')

IpCam = cv2.VideoCapture(0 , cv2.CAP_DSHOW)

while True:
    _,IpCamImg = IpCam.read()
    ImgResize = cv2.resize(IpCamImg, (0, 0), None, 0.4, 0.4)
    Color = cv2.cvtColor(ImgResize, cv2.COLOR_BGR2RGB)
    MultiScale = Cascade.detectMultiScale(
      Color,
      scaleFactor=1.1,
      minNeighbors=5,
      minSize=(30, 30),
      flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in MultiScale:
        cv2.rectangle(ImgResize, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Acer_Camera', ImgResize)
    Exit = cv2.waitKey(15) & 0xFF
    if Exit == 27:
        break

IpCamImg.release()
cv2.destroyAllWindows()
