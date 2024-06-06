#Enhancednoise reduction
import cv2
import matplotlib.pyplot as plt

# Read the binary thresholded image
img = cv2.imread('binary_otsu_thresholded.png', cv2.IMREAD_GRAYSCALE)  # Ensure it is read in grayscale

# Apply image denoising
dst = cv2.fastNlMeansDenoising(img, None, 10, 7, 21)  # Adjust parameters as needed

# Plot original and denoised image
titles = ["Original Image", "Denoised Image"]
images = [img, dst]

plt.figure(figsize=(10, 5))  # Adjusted for better visualization

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], 'gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()  # Show the plot

# Save only the denoised image
output_dir = r'/Users/kirankumar.kosanapogu/PycharmProjects/MLDataExtraction/OutPut/'  # Specify the directory
output_filename = 'denoised_image.png'
output_path = f"{output_dir}/{output_filename}"

# Ensure the output directory exists
if not cv2.os.path.exists(output_dir):
    cv2.os.makedirs(output_dir)

cv2.imwrite(output_path, dst)  # Save the denoised image
print(f"Denoised image saved as {output_path}")
