# HVACGraphicsClassifier
HVACGraphicsClassifier is an experimental tinyML project aimed at classifying HVAC control system graphics using computer vision. A project goal from the start is support of Tiny ML Micro, allowing models to be quantized to run on microcontrollers with the TensorFlow C library.


```bash
HVACGraphicsClassifier/
│
├── data/
│   ├── annotations/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   ├── images/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   └── labels.txt
│
├── models/
│   ├── hvac_classifier.h5
│   ├── hvac_classifier.tflite
│   └── hvac_classifier_quant.tflite
│
├── scripts/
│   ├── preprocess.py
│   └── train.py
│   └── convert_to_tflite.py
│
├── embedded/
│   ├── include/
│   │   ├── model.h
│   │   ├── input_preprocessing.h
│   │   ├── output_postprocessing.h
│   └── src/
│       ├── main.c
│       ├── model.c
│       ├── input_preprocessing.c
│       ├── output_postprocessing.c
│   └── Makefile
│
├── notebooks/
│   └── explore_data.ipynb
│
├── requirements.txt
└── README.md
```

## Project goals
Basic project goals
 - [ ] Compile BAS screenshots across many manufactures of typical HVAC system graphics
 - [ ] Perform image annotations with the labelImg tool to create ML dataset
 - [ ] Attempt at classifying whole screenshot HVAC system types with TF Lite Py computer vision
 - [ ] Attempt at classifying components inside the screenshots for ducts, pipes, sensor, valves, damper, fans, etc. with TF Lite Py computer vision
 - [ ] Attempt at classifying text on graphics which would represent I/O and setpoints with TF Lite Py computer vision
 - [ ] Attempt at classifying air or water flow direction with TF Lite Py computer vision?
 - [ ] Attempt at compiling text of classification(s) to inject into LLM for fault detection purposes with TF Lite Py computer vision
 - [ ] Attempt TF Lite Micro on embedded device like a [TensorFlow Lite for Microcontrollers Kit](https://www.adafruit.com/product/4317) with a quantized model
 