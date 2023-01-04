# Import Libraries
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from pathlib import Path
import argparse
import numpy
 
# Argument parsing variable declared
ap = argparse.ArgumentParser()
 
ap.add_argument("-i", "--image",
                required=True,
                help="Path to original data folder")
 
args = vars(ap.parse_args())
 
# Find all the images in the provided images folder
mypath = args["image"]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
images = numpy.empty(len(onlyfiles), dtype=object)
print("Total number of images: ", len(onlyfiles))
 
# Iterate through every image
# and resize all the images.

for n in range(0, len(onlyfiles)):
 
    path = join(mypath, onlyfiles[n])
    images[n] = cv2.imread(join(mypath, onlyfiles[n]),
                           cv2.IMREAD_UNCHANGED)
 
    # Load the image in img variable
    img = cv2.imread(path, 1)
 
    """
    # Define a resizing Scale
    # To declare how much to resize
    resize_scaling = 50
    resize_width = int(img.shape[1] * resize_scaling/100)
    resize_hieght = int(img.shape[0] * resize_scaling/100)
    resized_dimensions = (resize_width, resize_height)
 
    # Create resized image using the calculated dimensions
    resized_image = cv2.resize(img, resized_dimensions,
                               interpolation=cv2.INTER_AREA)
    """

    #get size
    height, width, channels = img.shape

    # Create a black image
    x = height if height > width else width
    y = height if height > width else width
    squared_image= np.zeros((x,y,3), np.uint8)
  
    squared_image[int((y-height)/2):int(y-(y-height)/2), int((x-width)/2):int(x-(x-width)/2)] = img

    # Save the image in Resize Folder
    cv2.imwrite(
      'resize/' + onlyfiles[n][0:-4] + '_resized.png', squared_image)
    
    if(n%500 == 0): print(f'{n} images resized successfully')
 