
# Import necessary libraries
import tkinter
import customtkinter
from tkinter import messagebox
import cv2
import matplotlib.pyplot as plt

# Initialize GUI settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Create the main window
app = customtkinter.CTk()
app.geometry("1000x500")
app.title("IPR_Assignment_1_BinaryPhoto")

# Label for threshold input
threshold_label = customtkinter.CTkLabel(app, text="Enter a threshold value between 0 and 255:")
threshold_label.pack(ipadx=10, ipady=10)

# Variable to store user-provided threshold
threshold_var = tkinter.StringVar()

# Entry field for threshold input
threshold_entry = customtkinter.CTkEntry(
    app,
    width=77,
    height=50,
    border_color="#ffffff",
    placeholder_text="Enter value"
)
threshold_entry.pack(padx=15, pady=15)

# Global variable to store the selected image path
global filepath


# Function to handle image path selection
# Prompts the user to select an image file using a file dialog.
def handle_path_input():
    global filepath
    filepath = customtkinter.filedialog.askopenfilename(
        title="Please select an image file",
        filetypes=[("All Images", "*.png;*.jpg;*.jpeg;*.svg;*.bmp;*.gif")]
    )


# Function to handle threshold value and display the binary image
def handle_threshold_value():
    """
    Retrieves user input, validates the threshold value, and calls the function from `MakePhotoBinary.py`.
    """
    try:
        input_threshold = int(threshold_entry.get())
        # Validate threshold value
        if input_threshold < 0:
            messagebox.showerror("Error", "Threshold value cannot be negative!")
            return
        if input_threshold > 255:
            messagebox.showerror("Error", "Threshold value cannot be greater than 255!")
            return

        # Call function from `MakePhotoBinary.py` with image path and threshold
        make_photo_binary(input_threshold, filepath)

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a numeric value.")
        
def make_photo_binary(input_threshold, filepath):
    # Image path:
    img_path = filepath

    # Read the image in BGR format (unchanged)
    original_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    # Convert to RGB for Matplotlib display (optional)
    original_img_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)

    # Create a grayscale copy
    grayscale_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

    # Thresholding with a value that user entered
    _, binary_img = cv2.threshold(grayscale_img, input_threshold, 255, cv2.THRESH_BINARY)

    
    # Create the figure with subplots
    rows = 1
    column = 2
    figure = plt.figure(figsize=(20, 10))

    figure.add_subplot(rows, column, 1)
    plt.imshow(original_img_rgb)
    plt.title("Original Image (Color)")

    figure.add_subplot(rows, column, 2)
    plt.imshow(binary_img, cmap="gray")  # Use "gray" colormap for grayscale display
    plt.title("Binary Image with Threshold = " + str(input_threshold))

    plt.tight_layout()  # Adjust layout for better visualization
    plt.show()


# Create buttons for selecting image and converting to binary
select_button = customtkinter.CTkButton(master=app, text="Select Image", command=handle_path_input)
select_button.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

convert_button = customtkinter.CTkButton(master=app, text="Display Binary Image", command=handle_threshold_value)
convert_button.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

# Start the GUI event loop
app.mainloop()
