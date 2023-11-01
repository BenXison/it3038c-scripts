from PIL import Image, ImageDraw, ImageFilter

# Open an image file
image = Image.open("flag2.jpg")

# 1. Resize the image
new_size = (300, 200)
resized_image = image.resize(new_size)

# 2. Rotate the image
rotated_image = resized_image.rotate(45)

# 3. Add text to the image
draw = ImageDraw.Draw(rotated_image)
text = "Hello, Pillow!"
draw.text((10, 10), text, fill="white")

# 4. Apply a filter (Blur)
filtered_image = rotated_image.filter(ImageFilter.BLUR)

# 5. Crop a portion of the image
left, top, right, bottom = 50, 50, 250, 150
cropped_image = filtered_image.crop((left, top, right, bottom))

# Display and save the final altered image
cropped_image.show()
cropped_image.save("output.jpg")

# Close the image files
image.close()
resized_image.close()
rotated_image.close()
filtered_image.close()
cropped_image.close()
