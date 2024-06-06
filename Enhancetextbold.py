#Bold
import pytesseract
from PIL import Image

# Open the image file
image = Image.open('denoised_image.png')

# Use pytesseract to extract text from the image
text = pytesseract.image_to_string(image)

# Function to print text in bold
def print_bold(text):
    print('\033[1m' + text + '\033[0m')

# Print the extracted text in bold
print_bold(text)
