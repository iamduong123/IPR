"""
A program to display the magnitude spectrum
from the FFT.
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
from PIL import Image


def ImgToFloat():

    img = cv2.imread("TUT2/public/tiger.jpg")

    img_array = plt.imread("TUT2/public/tiger.jpg").astype(float)

    return img, img_array

def FastFourierTransform(img_array):
    fourier_array = np.fft.fft2(img_array)
    return fourier_array

def displaySpecturm(fourier_array):
    spectrum = np.fft.fftshift(fourier_array)
    return spectrum

def specturmToImage(spectrum):
    original_img = np.fft.ifft2(spectrum)
    return original_img

def displayMultipleImage(img, spectrum, original_img):
    fig = plt.figure(figsize=(10, 7))

    row = 1
    column = 3


    fig.add_subplot(row, column, 1)
    plt.imshow(img)
    plt.title("Original image")


    fig.add_subplot(row, column, 2)
    plt.imshow( np.log(np.abs(spectrum)))
    plt.title("Magnitude spectrum")

    fig.add_subplot(row, column, 3)
    plt.imshow(np.abs(original_img))
    plt.title("Image after convert it back")

def display_menu():
  for i in range(0,1):
      print("\n")
  print("FFT Program Menu:")
  print("1. Run FFT analysis")
  print("2. Exit")
  choice = input("Enter your choice: ")
  return choice

def main():
  while True:
    choice = display_menu()
    if choice == "1":
      img, img_array = ImgToFloat()
      fourier_array = FastFourierTransform(img_array)
      spectrum = displaySpecturm(fourier_array)
      original_img = specturmToImage(spectrum)
      displayMultipleImage(img, spectrum, original_img)
      plt.show()
    elif choice == "2":
      print("Exiting program...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()