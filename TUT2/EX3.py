import cv2
import matplotlib.pyplot as plt
import numpy as np
def apply_sobel_operator(image):
    # Convert the image to grayscale if it's not already
    if len(image.shape) == 3:
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        grayscale_image = image

    # Apply the Sobel operator
    sobel_x = cv2.Sobel(grayscale_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(grayscale_image, cv2.CV_64F, 0, 1, ksize=3)

    # Combine the gradient components
    gradient_magnitude_x = cv2.magnitude(sobel_x, np.zeros_like(sobel_x))
    gradient_magnitude_y = cv2.magnitude(np.zeros_like(sobel_y), sobel_y)

    return gradient_magnitude_x, gradient_magnitude_y

def main():
    # Load an image
    image_path = 'v'
    original_image = cv2.imread(image_path)

    # Apply the Sobel operator
    edges_x, edges_y = apply_sobel_operator(original_image)

    # Display the original image and the edges using matplotlib
    plt.figure(figsize=(15, 5))

    plt.subplot(131)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')

    plt.subplot(132)
    plt.imshow(edges_x, cmap='gray')
    plt.title('Edges in X-direction (Sobel Operator)')

    plt.subplot(133)
    plt.imshow(edges_y, cmap='gray')
    plt.title('Edges in Y-direction (Sobel Operator)')

    plt.show()

if __name__ == "__main__":
    main()
