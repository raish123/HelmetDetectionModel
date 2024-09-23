# Mask Detection Model using VGG16

This project is a deep learning-based mask detection system that uses the VGG16 CNN model to classify whether a person is wearing a mask (`1`) or not (`0`). The model has been trained with two classes: `1` for wearing a mask and `0` for not wearing a mask.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [References](#references)

## Overview

The goal of this project is to build a robust image classification system that can detect whether a person in an image is wearing a mask. This can be useful for ensuring public safety in places where wearing masks is mandated, such as hospitals, airports, or during pandemics.

The VGG16 deep learning model, pre-trained on ImageNet, has been fine-tuned to detect face masks. The model takes images of people and predicts if they are complying with mask requirements.

## Dataset

The dataset used for training and validation consists of images with two labels:
1. **Mask** (`1`) - The person in the image is wearing a mask.
2. **No Mask** (`0`) - The person in the image is not wearing a mask.


## Model Architecture

This project leverages the **VGG16** model, a 16-layer Convolutional Neural Network (CNN), pre-trained on the ImageNet dataset. We have fine-tuned the model by adding fully connected layers on top of the VGG16 base to classify images into two classes: `mask` and `no mask`.

### Key Features:
- **VGG16**: Pre-trained model used as the base.
- **Transfer Learning**: Fine-tuned with mask/no-mask dataset.
- **Binary Classification**: Output layer has two neurons for predicting mask or no mask.

## Requirements

To run this project, you need the following libraries and tools:

- Python 3.7+
- TensorFlow
- Keras
- NumPy
- OpenCV (for image processing)
- Matplotlib (for visualization)
- Scikit-learn (for metrics and evaluation)

You can install the dependencies using:
```bash
pip install -r requirements.txt
