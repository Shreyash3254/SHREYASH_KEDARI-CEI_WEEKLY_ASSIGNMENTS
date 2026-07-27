# 🧠 Autoencoder for Image Denoising using MNIST

> ### 🎓 Celebal Excellence Internship (CEI) Program 2026
>
> **Deep Learning | Computer Vision | Autoencoders | TensorFlow | Image Denoising**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-DeepLearning-red?style=for-the-badge&logo=keras)
![Google Colab](https://img.shields.io/badge/Google-Colab-yellow?style=for-the-badge&logo=googlecolab)

</p>

---

# 📌 Project Overview

This repository contains my **Week 6 Deep Learning Assignment** completed as part of the **Celebal Excellence Internship (CEI) Program 2026**.

The objective of this project is to design and implement a **Convolutional Autoencoder** capable of removing Gaussian noise from handwritten digit images using the **MNIST** dataset. The model learns compact latent representations through an encoder-decoder architecture and reconstructs cleaner versions of noisy input images.

The notebook demonstrates the complete deep learning workflow, including data preprocessing, noise generation, model development, training, evaluation, and visualization.

---

# 🎯 Objectives

- Build a Convolutional Autoencoder
- Learn latent feature representations
- Remove Gaussian noise from images
- Evaluate reconstruction quality using quantitative metrics
- Visualize denoised image outputs

---

# 🏗️ Model Architecture

```text
Input Image (28×28×1)
        │
        ▼
Conv2D (32 Filters)
        │
Batch Normalization
        │
MaxPooling
        │
        ▼
Conv2D (64 Filters)
        │
Batch Normalization
        │
MaxPooling
        │
────────── Latent Space ──────────
        │
Conv2D (64 Filters)
        │
Batch Normalization
        │
UpSampling
        │
Conv2D (32 Filters)
        │
Batch Normalization
        │
UpSampling
        │
        ▼
Output Image (28×28×1)
```

---

# 🚀 Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Google Colab

---

# 📂 Dataset

**Dataset:** MNIST Handwritten Digits

- 60,000 Training Images
- 10,000 Testing Images
- Image Size: **28 × 28**
- Grayscale Images

Noise Applied:

- Gaussian Noise
- Noise Factor = **0.4**

---

# ⚙️ Model Configuration

| Parameter | Value |
|-----------|-------|
| Optimizer | Adam |
| Loss Function | Binary Crossentropy |
| Metric | Mean Squared Error (MSE) |
| Epochs | 20 |
| Batch Size | 128 |

---

# 📊 Evaluation Metrics

The trained model is evaluated using:

- ✅ Binary Crossentropy Loss
- ✅ Mean Squared Error (MSE)
- ✅ Peak Signal-to-Noise Ratio (PSNR)

---

# 📈 Visualizations Included

- 📊 Training vs Validation Loss
- 🖼 Original Images
- 🌧 Noisy Images
- ✨ Reconstructed Images
- 🎲 Random Test Predictions
- 🔥 Pixel-wise Error Heatmaps

---

# 🌍 Applications

- 🏥 Medical Image Enhancement
- 📄 Document Restoration
- 🛰 Satellite Image Processing
- 📷 Digital Camera Noise Reduction
- 🚗 Autonomous Vehicle Vision Systems
- 🔍 Industrial Defect Detection
- 📦 Image Compression
- 🤖 Feature Representation Learning

---

# 📁 Repository Structure

```
📦 Autoencoder-Image-Denoising-MNIST
│
├── 📓 Week6_<ShreyashKedari>.ipynb
├── 📄 README.md
├── 📂 images
│   ├── training_loss.png
│   ├── reconstruction.png
│   ├── error_heatmap.png
│   └── model_summary.png
└── 📄 requirements.txt
```

---

# 🚀 Future Improvements

- Variational Autoencoders (VAE)
- GAN-based Image Denoising
- Diffusion Models
- Residual Autoencoders
- Attention-based Networks
- Color Image Restoration

---

# 💡 Key Learnings

- Convolutional Autoencoders
- Latent Space Representation
- Image Denoising
- Gaussian Noise Simulation
- Feature Extraction
- TensorFlow/Keras Model Development
- Deep Learning Workflow

---

# 📚 References

- TensorFlow Documentation
- Keras Documentation
- MNIST Handwritten Digit Dataset
- Deep Learning by Ian Goodfellow
- Celebal Excellence Internship (CEI) Program 2026 Learning Resources

---

# 👨‍💻 Author

### **Shreyash Rohidas Kedari**

Dr. D. Y. Patil Institute of Technology, Pimpri, Pune

🎓 **Celebal Excellence Internship (CEI) Program 2026**


---

## ⭐ If you found this project useful, don't forget to star this repository!
