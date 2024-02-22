from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np

threshold_value = 132
def load_and_convert_to_grayscale(image_path):
    color_image_pil = Image.open(image_path)
    grayscale_image_pil = color_image_pil.convert('L')
    return color_image_pil, grayscale_image_pil

def load_binary_image(image_path):
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_image

def apply_erosion(image, structuring_element=cv2.MORPH_RECT):
    binary_array = np.array(image)
    kernel = cv2.getStructuringElement(structuring_element, (5, 5))
    eroded_array = cv2.erode(binary_array, kernel, iterations=1)
    eroded_image = Image.fromarray(eroded_array)
    return eroded_image

def apply_dilation(image, structuring_element=cv2.MORPH_RECT):
    binary_array = np.array(image)
    kernel = cv2.getStructuringElement(structuring_element, (5, 5))
    dilated_array = cv2.dilate(binary_array, kernel, iterations=1)
    dilated_image = Image.fromarray(dilated_array)
    return dilated_image

def perform_morphological_operations(image, operation_type, structuring_element=cv2.MORPH_RECT):
    binary_array = np.array(image)
    kernel = cv2.getStructuringElement(structuring_element, (5, 5))

    if operation_type == 'open':
        result_array = cv2.morphologyEx(binary_array, cv2.MORPH_OPEN, kernel)
    elif operation_type == 'close':
        result_array = cv2.morphologyEx(binary_array, cv2.MORPH_CLOSE, kernel)
    else:
        raise ValueError("Invalid operation type. Use 'open' or 'close'.")

    result_image = Image.fromarray(result_array)
    return result_image

def main():
    # Load the binary image from Exercise 1
    binary_image_path = 'TUT2/public/tiger.jpg'
    binary_image = load_binary_image(binary_image_path)

    # Task 1: Apply erosion using different structuring elements
    eroded_square = apply_erosion(binary_image, cv2.MORPH_RECT)
    eroded_circle = apply_erosion(binary_image, cv2.MORPH_ELLIPSE)

    # Task 2: Apply dilation using different structuring elements
    dilated_square = apply_dilation(binary_image, cv2.MORPH_RECT)
    dilated_circle = apply_dilation(binary_image, cv2.MORPH_ELLIPSE)

    # Task 3: Perform opening and closing operations
    opened_image = perform_morphological_operations(binary_image, 'open', cv2.MORPH_RECT)
    closed_image = perform_morphological_operations(binary_image, 'close', cv2.MORPH_RECT)

    # Display the original binary image and the results of morphological operations using matplotlib
    plt.figure(figsize=(8, 10))

    plt.subplot(331)
    plt.imshow(np.array(binary_image), cmap='gray')
    plt.title('Binary Image')

    plt.subplot(332)
    plt.imshow(np.array(eroded_square), cmap='gray')
    plt.title('Eroded (Square)')

    plt.subplot(333)
    plt.imshow(np.array(eroded_circle), cmap='gray')
    plt.title('Eroded (Circle)')

    plt.subplot(334)
    plt.imshow(np.array(dilated_square), cmap='gray')
    plt.title('Dilated (Square)')

    plt.subplot(335)
    plt.imshow(np.array(dilated_circle), cmap='gray')
    plt.title('Dilated (Circle)')

    plt.subplot(336)
    plt.imshow(np.array(opened_image), cmap='gray')
    plt.title('Opened Image')

    plt.subplot(338)
    plt.imshow(np.array(closed_image), cmap='gray')
    plt.title('Closed Image')

    plt.show()

if __name__ == "__main__":
    main()
