from PIL import Image

# Open the image and convert to grayscale
img = Image.open('om.jpeg').convert('L')  # 'L' mode for grayscale
pixelMap = img.load()

# Create a new image for the result
imgNew = Image.new(img.mode, img.size)
pixelNew = imgNew.load()

# Process pixel values
for i in range(img.size[0]):  # Width
    for j in range(img.size[1]):  # Height
        if 0 <= pixelMap[i, j] <= 31:
            pixelNew[i, j] = 0
        elif 32 <= pixelMap[i, j] <= 63:
            pixelNew[i, j] = 64
        elif 64 <= pixelMap[i, j] <= 95:
            pixelNew[i, j] = 128
        elif 96 <= pixelMap[i, j] <= 127:
            pixelNew[i, j] = 192
        else:
            pixelNew[i, j] = 255

# Save the modified image
imgNew.save('om_new.png')
