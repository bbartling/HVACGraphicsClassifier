import pytesseract
from PIL import Image
import cv2
import numpy as np
import os
import sys

'''
py -3.9 .\scripts\extract_text.py .\data\images\ahu_heat_broken_sim.jpg
'''

# Specify the path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\bbartling\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def image_to_text(image, region=None):
    if region:
        image = image[region[1]:region[3], region[0]:region[2]]
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(image)
    return text

def process_image(image_path):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # Define regions based on the provided layout
    regions = {
        'return_air': (width // 2, 0, width, height // 2),
        'exhaust_air': (0, 0, width // 2, height // 2),
        'outside_air': (0, height // 2, width // 2, height),
        'discharge_air': (width // 2, height // 2, width, height),
        'mixing_area': (width // 4, height // 4, 3 * width // 4, 3 * height // 4)
    }

    results = {}
    for region_name, region_coords in regions.items():
        text = image_to_text(image, region_coords)
        results[region_name] = text.strip()

    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_text.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]
    if not os.path.exists(image_path):
        print(f"File {image_path} does not exist.")
        sys.exit(1)

    results = process_image(image_path)
    for region_name, text in results.items():
        print(f"Region: {region_name}")
        print(f"Text found:\n{text}\n{'-'*40}")
