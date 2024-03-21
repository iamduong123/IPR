"""
A comprehensive Python program that creates a GUI for resizing images.
"""

# Import necessary libraries
import tkinter
import customtkinter
import cv2
from tkinter import messagebox

# Define the image resizing function
def image_resize(desired_height, desired_width, path_from_user):
    """
    Resizes an image using OpenCV.

    Args:
        desired_height (int): The desired height of the resized image.
        desired_width (int): The desired width of the resized image.
        path_from_user (str): The path to the image file.
    """

    # Read the image using OpenCV
    img = cv2.imread(path_from_user)

    # Resize the image using OpenCV's resize function
    resized_img = cv2.resize(img, (desired_height, desired_width), fx=0.1, fy=0.1)

    # Display the resized image using OpenCV
    cv2.imshow("Resized Image", resized_img)
    cv2.waitKey()

# Initialize the GUI with customtkinter
customtkinter.set_appearance_mode("dark")  # Set dark mode
customtkinter.set_default_color_theme("dark-blue")  # Set default button color

app = customtkinter.CTk()  # Create the main window
app.geometry("860x480")  # Set window size
app.title("IPR_Assignment 1_Resize Image")  # Set window title

# Create GUI elements
title_label = customtkinter.CTkLabel(app, text="Enter desired image dimensions:")
title_label.pack(ipadx=10, ipady=10)

height_var = tkinter.StringVar()
height_entry = customtkinter.CTkEntry(app, width=500, height=50, border_color="purple",
                                      placeholder_text="Enter the height:", placeholder_text_color="white")
height_entry.pack(padx=10, pady=10)

width_var = tkinter.StringVar()
width_entry = customtkinter.CTkEntry(app, width=500, height=50, border_color="violet",
                                     placeholder_text="Enter the width: ", placeholder_text_color="white")
width_entry.pack(padx=10, pady=10)

filepath = ""  # Global variable to store the selected image path

# Function to handle image path selection
def handle_path_input():
    """
    Prompts the user to select an image file using a file dialog.
    """
    global filepath
    filepath = customtkinter.filedialog.askopenfilename(
        title="Please select an image file",
        filetypes=[(("All Images", "*.png;*.jpg;*.jpeg;*.svg;*.bmp;*.gif"))]
    )

# Function to handle image resizing
def handle_resize():
    """
    Retrieve user input, validate dimensions, and call the image_resize function.
    """

    desired_height = int(height_entry.get())
    desired_width = int(width_entry.get())

    if desired_height < 0 or desired_width < 0:
        messagebox.showerror("Error", "Image dimensions cannot be negative")
        return

    image_resize(desired_height, desired_width, filepath)

# Create buttons for selecting image and resizing
select_button = customtkinter.CTkButton(master=app, text="Select Image", command=handle_path_input)
select_button.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

resize_button = customtkinter.CTkButton(master=app, text="Resize Image", command=handle_resize)
resize_button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

# Start the GUI event loop
app.mainloop()
