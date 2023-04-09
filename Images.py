from PIL import Image
import numpy as np
import random
# Open the PNG file
img = Image.open('Images/LinkedIn_logo_initials.png')
img2 = Image.open('Images/stonk.png')
# Convert the image to a PIL object
img_pil = img.convert('RGB')
img_pil2 = img2.convert('RGB')

img_pil1 = img_pil.convert('L')
img_pil2 = img_pil2.convert('L')
width1, height1 = img_pil1.size
width2, height2 = img_pil2.size
# Define the probability of adding noise to each pixel
noise_prob = 0.05

# Loop through each pixel in the image
for x in range(width1):
    for y in range(height1):

        # Check if noise should be added to this pixel
        if random.random() < noise_prob:
            # Generate a random value between 0 and 255
            noise_value = random.randint(0, 255)

            # Set the pixel to the noise value
            img_pil1.putpixel((x, y), noise_value)

for x in range(width2):
    for y in range(height2):

        # Check if noise should be added to this pixel
        if random.random() < noise_prob:
            # Generate a random value between 0 and 255
            noise_value = random.randint(0, 255)

            # Set the pixel to the noise value
            img_pil2.putpixel((x, y), noise_value)

img_array1 = np.array(img_pil1)
img_array2 = np.array(img_pil2)

# Generate Gaussian noise with the same shape as the image
mean = 0
variance = 10
gaussian1 = np.random.normal(mean, variance, img_array1.shape)
gaussian2 = np.random.normal(mean, variance, img_array2.shape)

# Add the Gaussian noise to the image array
img_array_with_noise1 = img_array1 + gaussian1
img_array_with_noise2 = img_array2 + gaussian2

# Convert the NumPy array back to a PIL object
img_with_noise1 = Image.fromarray(np.uint8(img_array_with_noise1))
img_with_noise2 = Image.fromarray(np.uint8(img_array_with_noise2))
# Display the image with noise added
img_with_noise1.show()
img_with_noise2.show()
img_pil1.show()
img_pil2.show()
img_with_noise1.save('Images/LinkedIn_G.png')
img_with_noise2.save('Images/Stonk_G.png')
img_pil1.save('Images/LinkedIn_SAP.png')
img_pil2.save('Images/Stonk_SAP.png')


