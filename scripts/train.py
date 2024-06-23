import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

def create_model(input_shape, num_classes):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model(data_dir, model_save_path, input_shape, batch_size=32, epochs=10):
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    train_generator = datagen.flow_from_directory(
        data_dir,
        target_size=input_shape[:2],
        batch_size=batch_size,
        class_mode='sparse',
        subset='training'
    )
    val_generator = datagen.flow_from_directory(
        data_dir,
        target_size=input_shape[:2],
        batch_size=batch_size,
        class_mode='sparse',
        subset='validation'
    )

    model = create_model(input_shape, num_classes=len(train_generator.class_indices))
    model.fit(train_generator, validation_data=val_generator, epochs=epochs)
    model.save(model_save_path)

if __name__ == "__main__":
    train_model(
        data_dir='data/images',
        model_save_path='models/hvac_classifier.h5',
        input_shape=(128, 128, 3),
        batch_size=32,
        epochs=10
    )
