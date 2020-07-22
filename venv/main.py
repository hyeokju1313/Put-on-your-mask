#  This Code write by RenSic_(OpenCV part), Wono(Arduio part)
#  Project Name '누구인가? 누가 마스크를 쓰지 않았느냔 말이야?!' (KR) 1.0.0-Beta

#  -*- coding:utf-8 -*-
#  -*- coding:cp949 -*-

import numpy as np
import cv2
import serial
import time

# Port Setting(Win)
port = 'COM5'

# Serial setting
baudrate = 9600
ard = serial.Serial(port, baudrate)

# Human Face data
xml = 'haarcascade_frontalface_default.xml'  # Recommend Path of the Data File(~~.xml or etc.) in same folder
face_cascade = cv2.CascadeClassifier(xml)  # create Object

# Use Laptop WebCam
cap = cv2.VideoCapture(0)

# Arduino code
# 'A' is considered Turn On & '1' by binary
# 'B' is considered Turn Off & '0' by binary
A = 1
B = 2

# int -> str (serial connect rule)
A = str(A)
B = str(B)

Trans1 = A
Trans1 = Trans1.encode('utf-8')
Trans2 = B
Trans2 = Trans2.encode('utf-8')

# OpenCV Human Face detection
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Left Right Symmetry
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # BGR -> GrayScale

    if len(faces):
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Put a square frame on a Human face
        ard.write(Trans1)  # Turn On LED
    else:
        ard.write(Trans2)  # Turn Off LED
    cv2.imshow('result', frame)

    k = cv2.waitKey(30) & 0xff

    if k == 27:  # Esc == Kill process
        break

cap.release()
cv2.destroyAllWindows()
