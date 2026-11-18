import cv2
image=cv2.imread("../lesson_01/Tony.jpeg")

pixel=image[50,100]
print(image.shape)
# Set one pixel to red (BGR)
image[50, 100] = [0, 0, 255]

# Create a solid green rectangle
image[100:200, 150:300] = [0, 255, 0]

cv2.imshow("Modified Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()