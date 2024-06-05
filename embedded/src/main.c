#include "tensorflow/lite/micro/all_ops_resolver.h"
#include "tensorflow/lite/micro/kernels/micro_ops.h"
#include "tensorflow/lite/micro/micro_error_reporter.h"
#include "tensorflow/lite/micro/micro_interpreter.h"
#include "tensorflow/lite/schema/schema_generated.h"
#include "tensorflow/lite/version.h"

#include "model.h"
#include "input_preprocessing.h"
#include "output_postprocessing.h"

#define MODEL_TFLITE_PATH "model/hvac_classifier_quant.tflite"
#define TENSOR_ARENA_SIZE 10 * 1024
#define IMAGE_WIDTH 128
#define IMAGE_HEIGHT 128
#define IMAGE_CHANNELS 3

uint8_t tensor_arena[TENSOR_ARENA_SIZE];

// Dummy image data for testing (normally you would load this from an external source)
uint8_t image_data[IMAGE_WIDTH * IMAGE_HEIGHT * IMAGE_CHANNELS];

int main() {
    // Set up logging
    static tflite::MicroErrorReporter micro_error_reporter;
    tflite::ErrorReporter* error_reporter = &micro_error_reporter;

    // Load the model
    const tflite::Model* model = tflite::GetModel(model_data);
    if (model->version() != TFLITE_SCHEMA_VERSION) {
        error_reporter->Report("Model provided is schema version %d not equal "
                               "to supported version %d.",
                               model->version(), TFLITE_SCHEMA_VERSION);
        return 1;
    }

    // Define operations resolver
    static tflite::AllOpsResolver resolver;

    // Build interpreter
    static tflite::MicroInterpreter interpreter(
        model, resolver, tensor_arena, TENSOR_ARENA_SIZE, error_reporter);

    // Allocate tensor memory
    TfLiteStatus allocate_status = interpreter.AllocateTensors();
    if (allocate_status != kTfLiteOk) {
        error_reporter->Report("AllocateTensors() failed");
        return 1;
    }

    // Get input and output tensors
    TfLiteTensor* input = interpreter.input(0);
    TfLiteTensor* output = interpreter.output(0);

    // Preprocess the image data
    preprocess_image(image_data, input->data.f, input->bytes / sizeof(float));

    // Run inference
    TfLiteStatus invoke_status = interpreter.Invoke();
    if (invoke_status != kTfLiteOk) {
        error_reporter->Report("Invoke failed");
        return 1;
    }

    // Postprocess and handle output data
    handle_output(output->data.f, output->bytes / sizeof(float));

    return 0;
}
