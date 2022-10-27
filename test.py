# # Import the necessary libraries
# from PIL import Image
# from numpy import asarray
 
 
# # load the image and convert into
# # numpy array
# img = Image.open('duck.jpeg')
# numpydata = asarray(img)
 
# # data
# print(numpydata)

# # Load image 
# filename = tf.constant("one.png")
# image_file = tf.read_file(filename)

# # Show Image
# Image("one.png")

# #convert method
# def convertRgbToWeight(rgbArray):
#     arrayWithPixelWeight = []
#     for i in range(int(rgbArray.size / rgbArray[0].size)):
#         for j in range(int(rgbArray[0].size / 3)):
#             lum = 255-((rgbArray[i][j][0]+rgbArray[i][j][1]+rgbArray[i][j][2])/3) # Reversed luminosity
#             arrayWithPixelWeight.append(lum/255) # Map values from range 0-255 to 0-1

#     return arrayWithPixelWeight



# # Convert image to numbers and print them
# image_decoded_png = tf.image.decode_png(image_file,channels=3)
# image_as_float32 = tf.cast(image_decoded_png, tf.float32)

# numpy.set_printoptions(threshold=numpy.nan)
# sess = tf.Session()
# squeezedArray = sess.run(image_as_float32)

# convertedList = convertRgbToWeight(squeezedArray)

# print(convertedList) # This will give me an array of numbers. 

import numpy as np
import cv2
import matplotlib.pyplot as plt

my_img = cv2.imread('duck.jpeg') 
inverted_img = (255.0 - my_img)  
final = inverted_img / 255.0

# Visualize the result
plt.imshow(final)
plt.show()

print(final.shape)
(661, 667, 3)