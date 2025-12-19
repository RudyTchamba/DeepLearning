import os
import cv2
import pickle
import numpy as np
import face_recognition

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imageBackground = cv2.imread('Resources/background.png')

# Importing the mode images into a list
folderModePath = 'Resources/Modes/'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
    
# print(len(imgModeList))

# Loading the encoding file

print('Loading Encode File ...')
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print('Encode File Loaded')

while True:
    success, img = cap.read()
    # We have to reduce the size of the image for faster processing
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    # Finding all the faces in the current frame
    faceCurFrame = face_recognition.face_locations(imgS)
    # Finding the encodings for the current frame
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
    
    # Loop through each face in the current frame and compare it with the known encodings
    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print("matches", matches)
        print("faceDis", faceDis)
        
        matchIndex = np.argmin(faceDis)
        
        if matches[matchIndex]:
            # print("Known Face Detected")
            studentId = studentIds[matchIndex]
            # print(studentId)
            
            y1, x2, y2, x1 = faceLoc
            # Since we reduced the size of the image, we have to multiply the coordinates by 4
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, f'{studentId}', (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            
            # Adding the mode image to the background
            imgModeList[1] = cv2.imread('Resources/Modes/3.png')
        else:
            # print("Unknown Face Detected")
            imgModeList[1] = cv2.imread('Resources/Modes/mode_unverified.png')
    
    
    imageBackground[162:162+480, 55:55+640] = img
    imageBackground[44:44+633, 808:808+414] = imgModeList[1]
    
    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imageBackground)
    cv2.waitKey(1)