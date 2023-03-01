from PIL import Image

img = Image.open('Image path')

img = img.convert('L')

nb_pixels_black = 0
width, height = img.size
for x in range(width):
    for y in range(height):
        if img.getpixel((x,y)) == 0:
            nb_pixels_black += 1

print("The number of black pixels in the image is : ", nb_pixels_black)
