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