import tensorflow as tf

def convert_to_tflite(model_path, tflite_model_path, quantize=False):
    model = tf.keras.models.load_model(model_path)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)

    if quantize:
        converter.optimizations = [tf.lite.Optimize.DEFAULT]

    tflite_model = converter.convert()

    with open(tflite_model_path, 'wb') as f:
        f.write(tflite_model)

if __name__ == "__main__":
    convert_to_tflite(
        model_path='models/hvac_classifier.h5',
        tflite_model_path='models/hvac_classifier_quant.tflite',
        quantize=True
    )
