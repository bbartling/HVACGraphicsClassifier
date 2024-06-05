import os
import shutil
import random
from sklearn.model_selection import train_test_split

def split_dataset(image_dir, annotation_dir, output_dir, test_size=0.2, val_size=0.1):
    images = [f for f in os.listdir(image_dir) if f.endswith('.jpg') or f.endswith('.png')]
    annotations = [f for f in os.listdir(annotation_dir) if f.endswith('.xml')]

    images.sort()
    annotations.sort()

    train_images, test_images, train_annotations, test_annotations = train_test_split(
        images, annotations, test_size=test_size, random_state=42)
    train_images, val_images, train_annotations, val_annotations = train_test_split(
        train_images, train_annotations, test_size=val_size, random_state=42)

    datasets = {
        'train': (train_images, train_annotations),
        'val': (val_images, val_annotations),
        'test': (test_images, test_annotations)
    }

    for dataset, (images, annotations) in datasets.items():
        os.makedirs(os.path.join(output_dir, 'images', dataset), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'annotations', dataset), exist_ok=True)

        for img, ann in zip(images, annotations):
            shutil.copy(os.path.join(image_dir, img), os.path.join(output_dir, 'images', dataset, img))
            shutil.copy(os.path.join(annotation_dir, ann), os.path.join(output_dir, 'annotations', dataset, ann))

if __name__ == "__main__":
    split_dataset(
        image_dir='data/images',
        annotation_dir='data/annotations',
        output_dir='data',
        test_size=0.2,
        val_size=0.1
    )
