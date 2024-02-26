import cv2
import matplotlib.pyplot as plt

def resize_and_threshold(image_path, output_path, width=300, height=300, threshold_value=127):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize the image
    resized_image = cv2.resize(image, (width, height))
    
    # Apply binary thresholding
    _, thresholded_image = cv2.threshold(resized_image, threshold_value, 255, cv2.THRESH_BINARY)
    
    # Plot the input and output images
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(thresholded_image, cmap='gray')
    plt.title('Thresholded Image')
    plt.axis('off')
    
    plt.show()
    
    # Save the resulting image
    cv2.imwrite(output_path, thresholded_image)
    
    print("Image processed successfully.")

if __name__ == "__main__":
    # Specify input and output image paths
    input_image_path = "ASM1/public/tiger.jpg"
    output_image_path = "ASM1/public/result.jpg"
    
    # Call the resize_and_threshold function with default parameters
    resize_and_threshold(input_image_path, output_image_path)
