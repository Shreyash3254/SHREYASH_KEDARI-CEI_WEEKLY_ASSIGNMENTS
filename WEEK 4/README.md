
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
├── WEEK4__Shreyash_Kedari_.ipynb
├── README.md
├── requirements.txt
└── images/
```

---

## ✅ Conclusion

- The ANN model successfully classified CIFAR-10 images but was limited because flattening images removes important spatial information.
- The CNN model achieved significantly better performance by learning local features such as edges, textures, and object shapes through convolutional layers.
- Increasing the number of convolution filters (32 → 64 → 128) enabled the network to learn richer feature representations.
- Applying EarlyStopping reduced overfitting by restoring the best-performing model during training.
- Data augmentation further improved generalization by exposing the model to transformed versions of training images.
- Overall, the CNN with data augmentation achieved the best performance, demonstrating why CNNs are the preferred choice for image classification tasks.

## Author

### **Shreyash Rohidas Kedari**

**Dr. D. Y. Patil Institute of Technology, Pimpri, Pune**

🚀 Celebal Excellence Internship (CEI) Program 2026
