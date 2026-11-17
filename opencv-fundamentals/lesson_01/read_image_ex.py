import cv2

image=cv2.imread("Tony.jpeg")

if image is None:
  raise FileNotFoundError("Could not find the file")

print("Shape: ", image.shape)
print("Data Type: ",image.dtype)
print("Height: ",image.shape[0])
print("Width: ",image.shape[1])

cv2.imshow("Original Image", image)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Back&White Image", gray)
cv2.waitKey(0)

cv2.destroyAllWindows()

