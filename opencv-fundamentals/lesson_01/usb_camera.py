import cv2
import time

cap=cv2.VideoCapture(0,cv2.CAP_V4L2)
if not cap.isOpened():
  raise RuntimeError("Couldnot open camera")

cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

previous_time=time.perf_counter()

while True:
  ret,frame=cap.read()
  if not ret:
    print("Failed to capture frame")
    break
  gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

  current_time=time.perf_counter()
  elapsed=current_time - previous_time
  previous_time=current_time

  fps=1.0 / elapsed if elapsed > 0 else 0.0

  cv2.putText(frame,f"FPS:{fps:.1f}",
              (20,40),
              cv2.FONT_HERSHEY_SIMPLEX,
              1,
              (0,255,0),
              2
              )
  cv2.imshow("Camera",frame)
  cv2.imshow("Grayscale",gray)

  if cv2.waitKey(1) & 0xFF==ord('f'):
    break

cap.release()
cv2.destroyAllWindows()