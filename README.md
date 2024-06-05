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

## Classification Visualization Goals
 ![Alt text](/image.JPG)

## Writeups on Linkedin
1. [Using the LLM to troubleshoot building automation](https://www.linkedin.com/posts/ben-bartling-510a0961_artificialintelligence-machinelearning-lexfridmanpodcast-activity-7200568805360615425-lVj9?utm_source=share&utm_medium=member_desktop)

## License
MIT License

Copyright (c) 2024 Ben Bartling

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

ADDITIONAL CYBERSECURITY NOTICE: Users are encouraged to apply the highest level of cybersecurity, OT, IoT, and IT measures when using this software. The authors and copyright holders disclaim any liability for cybersecurity breaches, mechanical equipment damage, financial damage, or loss of life arising from the use of the Software. Users assume full responsibility for ensuring the secure deployment and operation of the Software in their environments.