# Face-Detection-System
## 1. Import OpenCV<br>
cv2 is used for computer vision tasks like face detection.
## 2. Load Haar Cascade Classifier <br>
Loads a pre-trained Haar cascade model for detecting faces.
Ensure the correct path to the XML file.
## 3. Capture Video from Webcam<br>
cv2.VideoCapture(0) opens the default camera.
## 4. Process Video Frames Continuously<br>
Reads frames from the camera.
Converts each frame to grayscale for better detection.
## 5. Detect Faces in the Frame<br>
Uses detectMultiScale() to scan for faces.
scaleFactor=1.1 reduces image size gradually.
minNeighbors=5 filters out false positives.
minSize=(30,50) sets a minimum face size.
## 6. Draw Bounding Boxes Around Detected Faces<br>
Green rectangles are drawn around detected faces.
## 7. Display Video with Face Detection<br>
cv2.imshow() shows the live video feed with detection.
## 8. Exit the Program
Press 'a' to break the loop and close the webcam.
## 9. Release Resources & Close Windows<br>
Releases the webcam using video_cap.release().
Closes all OpenCV windows with cv2.destroyAllWindows().
