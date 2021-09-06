import cv2
import numpy as np
from pyzbar.pyzbar import decode
# --------------------------------------Scan with live cam----------------------
def VideoCap():
    cap=cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)

    while True:
        status,img=cap.read()
        for code in decode(img):
            # print(code.data,'\n',code.rect,'\n',code.polygon)
            # print('Decode data information \n')
            myData=code.data.decode('utf-8')
            print(myData)

            # for draw line
            polygonPoint = np.array([code.polygon], np.int32)
            polygonPoint = polygonPoint.reshape((-1, 1, 2))
            cv2.polylines(img, pts=[polygonPoint], isClosed=True, color=(255, 0, 0), thickness=3)

        cv2.imshow('QR Result',img)
        cv2.waitKey(1)

