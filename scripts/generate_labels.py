import os

def generate_labels_file(data_dir, output_file):
    class_names = sorted(os.listdir(data_dir))
    with open(output_file, 'w') as f:
        for idx, class_name in enumerate(class_names):
            f.write(f"{idx} {class_name}\n")

if __name__ == "__main__":
    data_dir = 'data/images'
    output_file = 'data/labels.txt'
    generate_labels_file(data_dir, output_file)
