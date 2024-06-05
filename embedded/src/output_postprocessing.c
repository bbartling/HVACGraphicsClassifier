#include "output_postprocessing.h"
#include <stdio.h>

void handle_output(float* output_data, int data_size) {
    // Example: Print the output data (class probabilities)
    for (int i = 0; i < data_size; ++i) {
        printf("Class %d: %f\n", i, output_data[i]);
    }
}
