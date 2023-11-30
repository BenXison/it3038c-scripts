from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont

# Open an image file
image_path = "flag2.jpg"
image = Image.open(image_path)

# 1. Resize the image to a larger size
new_size = (500, 350)
resized_image = image.resize(new_size)

# 2. Rotate the image
rotation_angle = 45
rotated_image = resized_image.rotate(rotation_angle)

# 3. Add semi-transparent text to the image with increased font size
draw = ImageDraw.Draw(rotated_image)
text = "God Bless America!!"
text_position = (50, 50)
text_color = (255, 0, 0)  # RGB color (red)
text_opacity = 150  # 0 (transparent) to 255 (opaque)
font_path = "arial.ttf"  # Change the font path as needed
font_size = 30  # Increased font size for better visibility
font = ImageFont.truetype(font_path, font_size)
draw.text(text_position, text, fill=text_color + (text_opacity,), font=font)

# 4. Apply multiple filters (Blur and Sharpen)
blurred_image = rotated_image.filter(ImageFilter.BLUR)
sharpened_image = blurred_image.filter(ImageFilter.SHARPEN)

# 5. Adjust the image contrast
contrast_factor = 2.0  # Increased for more contrast
enhancer = ImageEnhance.Contrast(sharpened_image)
contrasted_image = enhancer.enhance(contrast_factor)

# 6. Add a rectangle shape to the image
rectangle_position = (100, 100, 400, 250)  # (left, top, right, bottom)
rectangle_color = (0, 255, 0)  # RGB color (green)
rectangle_opacity = 100  # 0 (transparent) to 255 (opaque)
draw.rectangle(rectangle_position, fill=rectangle_color + (rectangle_opacity,))

# 7. Enhance color saturation
color_enhancer = ImageEnhance.Color(contrasted_image)
saturated_image = color_enhancer.enhance(1.5)  # Adjust the factor as needed

# Display and save the final altered image
saturated_image.show()
output_path = "flag2_updated.jpg"
saturated_image.save(output_path)

# Close the image files
image.close()
resized_image.close()
rotated_image.close()
blurred_image.close()
sharpened_image.close()
contrasted_image.close()
saturated_image.close()
