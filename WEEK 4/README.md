
# Week 4 - CIFAR-10 Image Classification using ANN & CNN

## Overview

This project demonstrates image classification on the CIFAR-10 dataset using two deep learning approaches:

- Artificial Neural Network (ANN)
- Convolutional Neural Network (CNN)

The objective is to understand why CNNs outperform traditional ANNs for image classification and to analyze the impact of different training strategies.

---

## Dataset

The CIFAR-10 dataset contains:

- 60,000 RGB images
- Image size: 32 × 32 × 3
- 10 object classes
- 50,000 training images
- 10,000 testing images

Classes:

- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

---

## Project Workflow

- Load CIFAR-10 Dataset
- Visualize Sample Images
- Data Preprocessing
- Build ANN Model
- Build CNN Model
- Compare Learning Curves
- Apply Data Augmentation
- Compare Model Performance
- Draw Conclusions

---

## Models Used

### Artificial Neural Network (ANN)

- Fully Connected Layers
- ReLU Activation
- Dropout
- Adam Optimizer
- EarlyStopping

---

### Convolutional Neural Network (CNN)

- Convolution Layers
- Batch Normalization
- Max Pooling
- Dropout
- EarlyStopping

---

## Training Improvements

Implemented the following enhancements:

- Increased ANN layers
- CNN Filters: 32 → 64 → 128
- EarlyStopping
- Increased training epochs
- Data Augmentation
- Batch Normalization
- Dropout Regularization

---

## Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- Pandas

---

## Results

The CNN significantly outperformed the ANN by preserving spatial information through convolutional layers.

Data augmentation further improved the model's ability to generalize on unseen images.

---

## Learning Outcomes

Through this project, I learned:

- Difference between ANN and CNN
- Image preprocessing techniques
- CNN architecture
- Batch Normalization
- Dropout
- Data Augmentation
- EarlyStopping
- Model evaluation and comparison

---

## Repository Structure

```
Week-4/
│
├── CIFAR10_ANN_CNN_Learning_Project.ipynb
├── README.md
├── requirements.txt
└── images/
```

---

## Author

**Shreyash Kedari**

Artificial Intelligence & Data Science

Celebal Technologies Internship
