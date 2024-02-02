def rotate_and_flip_image(image_path, save_path):
#     # Open the image file
#     original_image = Image.open(image_path)

#     # Rotate the image 90 degrees
#     rotated_image_90 = original_image.rotate(90)

#     # Rotate the image 180 degrees
#     rotated_image_180 = original_image.rotate(180)

#     # Horizontal flip
#     flipped_horizontal_image = original_image.transpose(Image.FLIP_LEFT_RIGHT)

#     # Vertical flip
#     flipped_vertical_image = original_image.transpose(Image.FLIP_TOP_BOTTOM)

#     # Save the rotated/flipped images
#     rotated_image_90.save(f'{save_path}/rotated_image_90.jpg')
#     rotated_image_180.save(f'{save_path}/rotated_image_180.jpg')
#     flipped_horizontal_image.save(f'{save_path}/flipped_horizontal_image.jpg')
#     flipped_vertical_image.save(f'{save_path}/flipped_vertical_image.jpg')

# rotate_and_flip_image("public/tiger.jpg", "public/tiger_rotate.jpg")
