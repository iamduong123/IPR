from PIL import Image, ImageEnhance, ImageFilter
#ex1
def convert_to_grayscale(image_path, output_path):
    img = Image.open(image_path)
    gray_img = img.convert('L')
    gray_img.save(output_path)
    print(f"Grayscale image saved as {output_path}")
convert_to_grayscale("TUT1/public/tiger.jpg", "TUT1/public/tiger_gray.jpg")
#ex2
def resize_img(image_path, output_path):
    img = Image.open(image_path)
    new_size = (75,90)
    re_img = img.resize(new_size)
    re_img.save(output_path)
    print(f"Resize image saved as {output_path}")
resize_img("TUT1/public/tiger.jpg", "TUT1/public/tiger_rs.jpg")
#ex3
def crop_img(image_path, output_path):
    img = Image.open(image_path)
    crop_box = (100, 100, 400, 400)
    crp_img = img.crop(crop_box)
    crp_img.save(output_path)
    print(f"crop image saved as {output_path}")
crop_img("TUT1/public/tiger.jpg", "TUT1/public/tiger_crp.jpg")
#ex4
def enhanced_img(image_path, output_path):
    img = Image.open(image_path)
    contrast_factor = 1.5  # Adjust as needed, 1.0 means no change
    contrast = ImageEnhance.Contrast(img)
    image_with_contrast = contrast.enhance(contrast_factor)
    brightness_factor = 1.2  # Adjust as needed, 1.0 means no change
    brightness = ImageEnhance.Brightness(image_with_contrast)
    image_with_brightness = brightness.enhance(brightness_factor)
    image_with_brightness.save(output_path)
    print(f"enhanced image saved as {output_path}")
enhanced_img("TUT1/public/tiger.jpg", "TUT1/public/tiger_enh.jpg")
#ex5
def rotate_and_flip_image(image_path, save_path):
 # Open the image file
    original_image = Image.open(image_path)
    # Rotate the image 90 degrees
    rotated_image_90 = original_image.rotate(90)
    rotated_image_90.save(f'{save_path}/rotated_image_90_{image_path.split("/")[-1]}')
    # Rotate the image 180 degrees
    rotated_image_180 = original_image.rotate(180)
    rotated_image_180.save(f'{save_path}/rotated_image_180_{image_path.split("/")[-1]}')
    # Horizontal flip
    flipped_horizontal_image = original_image.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_horizontal_image.save(f'{save_path}/flipped_horizontal_{image_path.split("/")[-1]}')
    # Vertical flip
    flipped_vertical_image = original_image.transpose(Image.FLIP_TOP_BOTTOM)
    flipped_vertical_image.save(f'{save_path}/flipped_vertical_{image_path.split("/")[-1]}')
rotate_and_flip_image("TUT1/public/tiger.jpg", "TUT1/public")

#ex6
def apply_filters(image_path, save_path):
    original_image = Image.open(image_path)
    blurred_image = original_image.filter(ImageFilter.BLUR)
    sharpened_image = original_image.filter(ImageFilter.SHARPEN)
    blurred_image.save(f'{save_path}/blurred_image.jpg')
    sharpened_image.save(f'{save_path}/sharpened_image.jpg')
apply_filters("TUT1/public/tiger.jpg", "TUT1/public")

