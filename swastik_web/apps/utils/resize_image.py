from PIL import Image
import os

# Set the input and output directories
input_dir = "/Users/pranavjha/Library/CloudStorage/GoogleDrive-pranajh7@gmail.com/My Drive/Projects/Swastik/swastik_web/apps/static/assets/img/nutrition/pics/"
output_dir = "/Users/pranavjha/Library/CloudStorage/GoogleDrive-pranajh7@gmail.com/My Drive/Projects/Swastik/swastik_web/apps/static/assets/img/nutrition/"

# Set the desired output size
output_size = (100, 60)

# Loop through all the files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # Open the image file
        image = Image.open(os.path.join(input_dir, filename))
        
        # Resize the image to the desired size
        resized_image = image.resize(output_size)
        
        # Save the resized image to the output directory
        resized_image.save(os.path.join(output_dir, filename))