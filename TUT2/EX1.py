from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np

def load_and_convert_to_grayscale(image_path):
    color_image_pil = Image.open(image_path)
    grayscale_image_pil = color_image_pil.convert('L')
    return color_image_pil, grayscale_image_pil

def apply_global_threshold(image, threshold_value):
    grayscale_array = np.array(image)
    _, binary_array = cv2.threshold(grayscale_array, threshold_value, 255, cv2.THRESH_BINARY)
    binary_image = Image.fromarray(binary_array)
    return binary_image

def main():
    # Task 1: Load a color image and convert it to grayscale
    image_path = 'TUT2/public/tiger.jpg'
    color_image_pil, grayscale_image_pil = load_and_convert_to_grayscale(image_path)

    # Task 2: Apply global thresholding to create a binary image
    threshold_value = 130
    binary_image_pil = apply_global_threshold(grayscale_image_pil, threshold_value)

    # Display the original color image, grayscale image, and binary image using matplotlib
    plt.figure(figsize=(10, 5))

    plt.subplot(131)
    plt.imshow(np.array(color_image_pil), cmap='gray')
    plt.title('Color Image')

    plt.subplot(132)
    plt.imshow(np.array(grayscale_image_pil), cmap='gray')
    plt.title('Grayscale Image')

    plt.subplot(133)
    plt.imshow(np.array(binary_image_pil), cmap='gray')
    plt.title('Binary Image')

    plt.show()

if __name__ == "__main__":
    main()
