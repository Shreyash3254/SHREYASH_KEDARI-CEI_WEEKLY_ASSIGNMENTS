# 🚀 Text Generation using RNN, LSTM & GRU

> **A Deep Learning project that explores sequence modeling and text generation using Vanilla RNN, LSTM, and GRU architectures with TensorFlow & Keras.**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=flat-square&logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red?style=flat-square&logo=keras)
![NLP](https://img.shields.io/badge/NLP-Text%20Generation-success?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

# 📖 Project Overview

Text generation is one of the fundamental applications of **Natural Language Processing (NLP)**.

In this project, three different recurrent neural network architectures—

- 🔹 Vanilla RNN
- 🔹 Long Short-Term Memory (LSTM)
- 🔹 Gated Recurrent Unit (GRU)

—are trained on a custom text corpus to learn language patterns and generate meaningful text sequences.

The project demonstrates how recurrent neural networks understand sequential information and predict the next word based on previous context.

---

# 🎯 Objectives

- Understand sequence modeling
- Learn text preprocessing techniques
- Implement RNN, LSTM, and GRU
- Compare model performance
- Generate meaningful text using trained models
- Visualize training loss

---

# 🧠 Project Workflow

```text
Custom Text Corpus
        │
        ▼
Text Preprocessing
        │
        ▼
Tokenization
        │
        ▼
Sequence Generation
        │
        ▼
Padding
        │
        ▼
Embedding Layer (64 Dimensions)
        │
        ▼
 ┌──────────────┐
 │ Vanilla RNN  │
 └──────────────┘
        │
 ┌──────────────┐
 │     LSTM     │
 └──────────────┘
        │
 ┌──────────────┐
 │      GRU     │
 └──────────────┘
        │
        ▼
Softmax Prediction
        │
        ▼
Generated Text
```

---

# 📂 Repository Structure

```text
Text-Generation-RNN-LSTM-GRU/
│
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
└── notebooks/
    └── Text_Generation_RNN_LSTM_GRU.ipynb
```

---

# ⚙️ Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Jupyter Notebook

---

# 📚 Project Features

✅ Custom text corpus

✅ Text tokenization

✅ Sequence generation

✅ Word embedding

✅ Vanilla RNN implementation

✅ LSTM implementation

✅ GRU implementation

✅ Training loss comparison

✅ Text generation

---

# 🏗 Model Architecture

Each model consists of:

```
Embedding Layer (64)
        ↓
RNN / LSTM / GRU (128 Units)
        ↓
Dense Layer
        ↓
Softmax Output
```

---

# 📈 Training Configuration

| Parameter | Value |
|-----------|-------|
| Embedding Dimension | **64** |
| Hidden Units | **128** |
| Epochs | **200** |
| Optimizer | Adam |
| Loss Function | Sparse Categorical Crossentropy |

---

# 📊 Model Comparison

| Model | Advantages |
|--------|------------|
| Vanilla RNN | Simple architecture for sequence learning |
| LSTM | Handles long-term dependencies effectively |
| GRU | Faster training with comparable performance |

---

# 📝 Sample Generated Text

### Input

```text
Artificial Intelligence
```

### Generated (GRU)

```text
Artificial intelligence allows machines to learn from data and make intelligent decisions
```

> *Generated text may vary slightly each time due to random initialization.*

---

# 📉 Training Loss

The notebook compares the training loss of:

- Vanilla RNN
- LSTM
- GRU

All three models successfully converge after **200 epochs**, demonstrating effective learning of the text corpus.

---

# 🎓 Student Learning Tasks Completed

- ✅ Replaced the original corpus with a custom paragraph
- ✅ Increased embedding dimension from **32 → 64**
- ✅ Increased hidden units from **64 → 128**
- ✅ Increased training epochs from **100 → 200**
- ✅ Generated **10 words** instead of 5

---

# 💡 Learning Outcomes

Through this project, I gained hands-on experience with:

- Natural Language Processing (NLP)
- Sequence Modeling
- Tokenization
- Word Embeddings
- Recurrent Neural Networks
- Long Short-Term Memory Networks
- Gated Recurrent Units
- Language Modeling
- Text Generation
- Deep Learning using TensorFlow & Keras

---

# 🚀 Future Improvements

- Train on a larger dataset
- Use pretrained word embeddings (Word2Vec / GloVe)
- Implement Bidirectional LSTM
- Apply Beam Search for better text generation
- Explore Transformer-based architectures
- Fine-tune GPT-style language models

---

# 🎯 Applications

- AI Chatbots
- Smart Text Completion
- Story Generation
- Content Writing
- Virtual Assistants
- Email Suggestions
- Language Modeling

---

# 👨‍💻 Author

**Shreyash Rohidas Kedari**

B.E. Artificial Intelligence & Data Science  
Dr. D. Y. Patil Institute of Technology, Pimpri  
Pune, Maharashtra

---

# 🙏 Acknowledgements

- Celebal Technologies Internship Program
- TensorFlow Documentation
- Keras Documentation
- Python Open Source Community

---

## ⭐ If you found this project useful, consider giving it a star!

> *"Every intelligent language model begins by learning one word at a time."* 🚀
