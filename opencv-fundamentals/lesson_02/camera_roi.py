import cv2
cap=cv2.VideoCapture(0)
if not cap.isOpened():
  raise RuntimeError("Camera not found")

while True:
  ret,frame=cap.read()

  if not ret:
    print("Failed to capture frame")
    break
  height,width=frame.shape[:2]
  y_start= int(height * 0.75)

  roi=frame[y_start:height,0:width]
  cv2.rectangle(frame,(0,y_start),(width-1,height-1),(0,255,0),2)
  cv2.imshow("Robot Camera",frame)
  cv2.imshow("Region of interest",roi)
  if cv2.waitKey(1) &  0xFF==ord('q'):
    break

cap.release()
cv2.destroyAllWindows()