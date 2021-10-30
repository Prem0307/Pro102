
# importing the module
from PIL import Image
import os
  
# importing the image 
im = Image.open("geeksforgeeks.jpg")
print("The size of the image before conversion : ", end = "")
print(os.path.getsize("geeksforgeeks.jpg"))
  
# converting to jpg
rgb_im = im.convert("RGB")
  
# exporting the image
rgb_im.save("geeksforgeeks_jpg.jpg")
print("The size of the image after conversion : ", end = "")
print(os.path.getsize("geeksforgeeks_jpg.jpg"))