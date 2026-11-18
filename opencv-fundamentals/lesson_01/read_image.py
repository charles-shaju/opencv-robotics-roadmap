from pathlib import Path

import cv2

image_path = Path(__file__).with_name("Tony.jpeg")
image = cv2.imread(str(image_path))

if image is None:
    raise FileNotFoundError(f"Could not find {image_path}")

print("Shape:", image.shape)
print("Data type:", image.dtype)
print("Height:", image.shape[0])
print("Width:", image.shape[1])

cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

