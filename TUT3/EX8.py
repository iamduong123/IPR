import cv2
import matplotlib.pyplot as plt

# Load the low-contrast image
image = cv2.imread('TUT3/public/tiger.jpg', cv2.IMREAD_GRAYSCALE)

# Create a CLAHE object (Arguments are optional and can be adjusted as needed)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# Apply CLAHE to the image
clahe_image = clahe.apply(image)

# Display the original and CLAHE-enhanced images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(clahe_image, cmap='gray')
plt.title('CLAHE Enhanced Image')
plt.axis('off')

plt.show()
