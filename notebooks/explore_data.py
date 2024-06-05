# explore_data.ipynb

# TODO Make into ipynb

# This notebook is for exploring the HVAC classification dataset.
# It includes visualizations and analysis to understand the data better.

import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import xml.etree.ElementTree as ET
import pandas as pd

# Paths to data directories
image_dir = '../data/images/train'
annotation_dir = '../data/annotations/train'

# Function to parse XML annotation files
def parse_annotation(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    objects = []
    for obj in root.findall('object'):
        obj_struct = {}
        obj_struct['name'] = obj.find('name').text
        bbox = obj.find('bndbox')
        obj_struct['bbox'] = [
            int(bbox.find('xmin').text),
            int(bbox.find('ymin').text),
            int(bbox.find('xmax').text),
            int(bbox.find('ymax').text)
        ]
        objects.append(obj_struct)
    return objects

# List some sample images and their annotations
sample_images = os.listdir(image_dir)[:5]

fig, axs = plt.subplots(len(sample_images), 1, figsize=(10, 15))
for img, ax in zip(sample_images, axs):
    img_path = os.path.join(image_dir, img)
    annotation_path = os.path.join(annotation_dir, img.replace('.jpg', '.xml'))
    
    image = mpimg.imread(img_path)
    ax.imshow(image)
    
    if os.path.exists(annotation_path):
        objects = parse_annotation(annotation_path)
        for obj in objects:
            bbox = obj['bbox']
            ax.add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2] - bbox[0], bbox[3] - bbox[1], fill=False, edgecolor='red', linewidth=2))
            ax.text(bbox[0], bbox[1] - 2, obj['name'], bbox=dict(facecolor='yellow', alpha=0.5), fontsize=12, color='black')
    
    ax.axis('off')
plt.show()

# Analyze class distribution
def analyze_class_distribution(annotation_dir):
    classes = []
    for ann_file in os.listdir(annotation_dir):
        if ann_file.endswith('.xml'):
            annotation_path = os.path.join(annotation_dir, ann_file)
            objects = parse_annotation(annotation_path)
            for obj in objects:
                classes.append(obj['name'])
    
    class_distribution = pd.Series(classes).value_counts()
    return class_distribution

class_distribution = analyze_class_distribution(annotation_dir)
print(class_distribution)

# Visualize class distribution
plt.figure(figsize=(10, 6))
class_distribution.plot(kind='bar')
plt.title('Class Distribution')
plt.xlabel('Class')
plt.ylabel('Frequency')
plt.show()

# Display random image with annotation
import random

random_img = random.choice(sample_images)
img_path = os.path.join(image_dir, random_img)
annotation_path = os.path.join(annotation_dir, random_img.replace('.jpg', '.xml'))

image = mpimg.imread(img_path)
plt.figure(figsize=(10, 10))
plt.imshow(image)

if os.path.exists(annotation_path):
    objects = parse_annotation(annotation_path)
    for obj in objects:
        bbox = obj['bbox']
        plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2] - bbox[0], bbox[3] - bbox[1], fill=False, edgecolor='red', linewidth=2))
        plt.text(bbox[0], bbox[1] - 2, obj['name'], bbox=dict(facecolor='yellow', alpha=0.5), fontsize=12, color='black')

plt.axis('off')
plt.show()
