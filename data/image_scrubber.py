import os
from PIL import Image

def scrub_metadata(image_path):
    with Image.open(image_path) as img:
        data = list(img.getdata())
        new_img = Image.new(img.mode, img.size)
        new_img.putdata(data)
        new_img.save(image_path)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                image_path = os.path.join(root, file)
                try:
                    scrub_metadata(image_path)
                    print(f"Metadata scrubbed for {image_path}")
                except Exception as e:
                    print(f"Failed to scrub metadata for {image_path}: {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    process_directory(current_directory)
