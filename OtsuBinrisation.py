#use this code for binary process
import cv2
import os

# Load the image in grayscale
img = cv2.imread('Sample7.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image has been loaded correctly
if img is None:
    raise FileNotFoundError("The specified image file does not exist.")

# Apply Otsu's thresholding
ret3, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Specify the directory to save the thresholded image
output_dir = r'/Users/kirankumar.kosanapogu/PycharmProjects/MLDataExtraction/OutPut/'  # Adjust this to your desired folder path
output_filename = 'binary_otsu_thresholded.png'
output_path = f"{output_dir}/{output_filename}"

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_output_dir)

# Save the thresholded image using OpenCV
cv2.imwrite(output_path, th1)

# Print confirmation
print(f"Thresholded image saved as {output_path}")
