#code by: VEDANT H. PAWAR
#ig: @vedant.time

from PIL import Image, ImageDraw, ImageFont

# Create A4 size image
# Define constants for page size and margin
MARGIN = 100 # margin in pixels
page_width, page_height = 2480, 3508  # in pixels
dpi = 300  # dots per inch
img = Image.new("RGB", (page_width, page_height), "white")
draw = ImageDraw.Draw(img)

# Define font and line spacing
font = ImageFont.truetype("C:/Users/admin/Desktop/handw/Handlee-Regular.ttf", size=56)
line_spacing = 50

# Generate ruled lines
num_lines = int((page_height - 2 * MARGIN) / line_spacing)
for i in range(num_lines):
    line_y = MARGIN + i * line_spacing
    draw.line((0, line_y, page_width, line_y), fill="gray", width=1)

# Compute the available space for the text
text_width = page_width - 2 * MARGIN
text_height = page_height - 2 * MARGIN

# Write the text on the lines
text = """Python Pillow Library: A Comprehensive Guide
Python Pillow is a popular image processing library used for opening, manipulating, and saving different types of image files.
It is built on top of the Python Imaging Library (PIL) and provides a simple and intuitive interface to perform image processing tasks.
In this article, we will explore the different features and functionalities of the Python Pillow library and how it can be used for various image processing tasks.

Opening and Saving Images

The Image module in Pillow provides functions for opening and saving various types of image files.
You can use the Image.open() function to open an image file and the Image.save() function to save an image to a file.

Resizing and Cropping Images

The Pillow library provides functions for resizing and cropping images. You can use the Image.resize() function to resize an image to a specific size, and the Image.crop() function to crop an image to a specific area.

Image Filtering and Enhancement

Pillow also provides a wide range of image filtering and enhancement functions that can be used to improve the quality of images.
You can use the ImageFilter module to apply different types of filters to an image, such as blur, contour, and edge enhancement.

Python Pillow is a powerful library that provides a wide range of image processing functions.
In this article, we covered some of the basic features of the Pillow library, such as opening and saving images, resizing and cropping images, and applying image filters and enhancements.
With Pillow, you can easily perform complex image processing tasks in your Python applications.
"""

# Split the text into lines that fit on the paper
lines = []
current_line = ""
for word in text.split():
    if font.getsize(current_line + " " + word)[0] < text_width:
        current_line += " " + word
    else:
        lines.append(current_line.strip())
        current_line = word
if current_line:
    lines.append(current_line.strip())

# Write the lines on the image
x, y = MARGIN, MARGIN
for line in lines:
    draw.text((x, y), line, fill="black", font=font)
    y += line_spacing

# Save the image
img.save("handwr1010.png")
print("Image generated successfully")


#code by: VEDANT H. PAWAR
#ig: @vedant.time