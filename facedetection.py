import cv2

face_cap = cv2.CascadeClassifier('C:/Users/klasy/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

# opens default video camera
video_cap = cv2.VideoCapture(0)
while True:
    # reads frames from camera
    ret, video_data = video_cap.read()
    # conversion into grayscale for better detection
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)

    # detects for faces
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1, # reduces image size
        minNeighbors=5, # reduces false positives
        minSize=(30,50), # sets min face size
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # draws green rectangles around the faces
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)

    # shows live feed with detection
    cv2.imshow('video_live',video_data)
    
    if cv2.waitKey(10) == ord('a'):
        # The camera closes when we press 'a'
        break

video_cap.release()


# For Enabling Camera
# video_cap = cv2.VideoCapture(0)
# while True:
#     ret, video_data = video_cap.read()
#     cv2.imshow('video_live',video_data)
#     if cv2.waitKey(10) == ord('a'):
#         # The camera closes when we press 'a'
#         break

# video_cap.release()
