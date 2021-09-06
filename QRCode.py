import cv2
import numpy as np
from pyzbar.pyzbar import decode

img=cv2.imread('IDCard.jpeg')


# =========================================Details=========================================
# d_img=decode(img)
# print(d_img)

# ----------for image scan--------------

for code in decode(img):
    print(code.data,'\n',code.rect,'\n',code.polygon)
    # print('Decode data information \n')
    QRdata = code.data.decode('utf-8')
    print(QRdata)
    print(code.polygon)
    polygonPoint=np.array([code.polygon],np.int32)
    # print(polygonPoint)
    # print(polygonPoint.shape)
    polygonPoint=polygonPoint.reshape((-1,1,2))
    # print(polygonPoint.shape)
    cv2.polylines(img,pts=[polygonPoint],isClosed=True,color=(255,0,0),thickness=3)

    PointRec=code.rect
    cv2.putText(img,QRdata,(PointRec[0],PointRec[1]),
                cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),3,)


cv2.imshow('QR Code',img)
cv2.waitKey(0)

