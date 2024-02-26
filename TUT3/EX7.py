import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('TUT3/public/tiger.jpg')

# Convert from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert from RGB to HSV
hsv_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)

# Convert from RGB to YCbCr
ycbcr_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)

# Display the separate channels of each color space
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

# Plot HSV channels
axes[0, 0].imshow(hsv_image[:, :, 0], cmap='hsv', vmin=0, vmax=179)
axes[0, 0].set_title('HSV - Hue')
axes[0, 1].imshow(hsv_image[:, :, 1], cmap='gray', vmin=0, vmax=255)
axes[0, 1].set_title('HSV - Saturation')
axes[0, 2].imshow(hsv_image[:, :, 2], cmap='gray', vmin=0, vmax=255)
axes[0, 2].set_title('HSV - Value')

# Plot YCbCr channels
axes[1, 0].imshow(ycbcr_image[:, :, 0], cmap='gray', vmin=0, vmax=255)
axes[1, 0].set_title('YCbCr - Y')
axes[1, 1].imshow(ycbcr_image[:, :, 1], cmap='gray', vmin=0, vmax=255)
axes[1, 1].set_title('YCbCr - Cb')
axes[1, 2].imshow(ycbcr_image[:, :, 2], cmap='gray', vmin=0, vmax=255)
axes[1, 2].set_title('YCbCr - Cr')

plt.tight_layout()
plt.show()
