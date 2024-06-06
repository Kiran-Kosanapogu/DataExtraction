import cv2
import os
import pytesseract
from PIL import Image
import json
import re

def apply_otsu_thresholding(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Otsu's thresholding
    ret3, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return th1

def apply_image_denoising(img):
    # Apply image denoising
    dst = cv2.fastNlMeansDenoising(img, None, 10, 7, 21)  # Adjust parameters as needed
    return dst

def extract_text_from_image(img):
    # OpenCV image to PIL image
    pil_img = Image.fromarray(img)

    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(pil_img)
    return text

def print_text_bold(text):
    # Function to print text in bold
    print('\033[1m' + text + '\033[0m')

def extract_specific_info(text):
    """Extract specific information such as name, father's name, mother's name, and sex."""
    info = {}
    patterns = {
        'Name': re.compile(r"Name\s*:\s*(.+)|Name\s+(.+)", re.IGNORECASE),
        "Name of Father": re.compile(r"Father\s*:\s*(.+)|Father\s+(.+)", re.IGNORECASE),
        "Name of Mother": re.compile(r"Mother\s*:\s*(.+)|Mother\s+(.+)", re.IGNORECASE),
        "Sex": re.compile(r"Sex\s*:\s*(.+)|Sex\s+(.+)", re.IGNORECASE),
        "Surname": re.compile(r"Surname\s*:\s*(.+)|Surname\s+(.+)", re.IGNORECASE),
        "Nationality": re.compile(r"Nationality\s*:\s*(.+)|Nationality\s+(.+)", re.IGNORECASE),
        "Place of Birth": re.compile(r"Place of Birth\s*:\s*(.+)|Place of Birth\s+(.+)", re.IGNORECASE),
        "First Name": re.compile(r"First Name\s*:\s*(.+)|First Name\s+(.+)", re.IGNORECASE),
        "Date of Birth": re.compile(r"Date of Birth\s*:\s*(.+)|Date of Birth\s+(.+)", re.IGNORECASE),
        "Certificate Id": re.compile(r"Certificate Id\s*:\s*(.+)|Certificate Id\s+(.+)", re.IGNORECASE)
    }
    
    for key, pattern in patterns.items():
        match = pattern.search(text)
        if match:
            # Extract the matched group which is not None
            info[key] = match.group(1) if match.group(1) else match.group(2)
            # Remove colon if present
            if info[key]:
                info[key] = info[key].strip(':')
    
    return info

def process_image(input_image_path, output_folder):
    try:
        # Load the image for pre-processing
        img = cv2.imread(input_image_path)

        if img is None:
            print(f"Error: Unable to read image {input_image_path}. Skipping...")
            return

        # Apply binary thresholding
        binary_img = apply_otsu_thresholding(img)

        # Apply image denoising
        denoised_img = apply_image_denoising(binary_img)

        # Extract text from denoised image
        text = extract_text_from_image(denoised_img)

        # Print the total extracted text in bold
        print("Total Extracted Text:")
        print_text_bold(text)

        # Extract specific information
        extracted_info = extract_specific_info(text)

        # Save extracted information to JSON file
        output_json_path = os.path.join(output_folder, os.path.basename(input_image_path).replace(".", "_info.") + "json")
        with open(output_json_path, 'w') as json_file:
            json.dump(extracted_info, json_file, indent=4)
        print(f"Extracted information saved as {output_json_path}")

    except Exception as e:
        print(f"Error processing image {input_image_path}: {str(e)}")

def process_images(input_folder, output_folder):
    
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith((".png", ".jpg", ".jpeg", "JPG", "JPEG",)):
            input_image_path = os.path.join(input_folder, filename)
            process_image(input_image_path, output_folder)

if __name__ == "__main__":
    input_folder = r'/Users/kirankumar.kosanapogu/PycharmProjects/MLDataExtraction/Samples/'
    output_folder = r'/Users/kirankumar.kosanapogu/PycharmProjects/MLDataExtraction/OutPut/'
    
    process_images(input_folder, output_folder)
