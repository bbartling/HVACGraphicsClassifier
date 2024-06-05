#include "input_preprocessing.h"

// Example preprocessing function: normalize image data to the range [0, 1]
void preprocess_image(uint8_t* image_data, float* input_data, int input_size) {
    for (int i = 0; i < input_size; ++i) {
        input_data[i] = image_data[i] / 255.0f;
    }
}
