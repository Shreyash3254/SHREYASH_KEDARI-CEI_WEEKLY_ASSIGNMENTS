
# 🚗 Tesla Sales & Delivery Forecasting
## 📊 End-to-End Machine Learning Pipeline

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikit-learn)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-EDA-green?style=for-the-badge)

### 🎓 Celebal Technologies Internship – Week 2 Assignment

### 👨‍💻 Shreyash Kedari
**Internship ID:** CT_CSI_DS_912

Dr. D. Y. Patil Institute of Technology, Pimpri

</div>

---

# 📖 Project Overview

This project presents a complete **End-to-End Machine Learning Pipeline** developed during the **Celebal Technologies Internship**.

The objective is to analyze Tesla's EV production and delivery data, perform extensive data preprocessing, build predictive machine learning models, optimize model performance, and forecast future deliveries using time series analysis.

The notebook follows an industry-standard machine learning workflow, making it suitable as both an internship assignment and a portfolio project.

---

# 🖼️ Project Gallery

### 📖 Project Cover

![Cover Page](images/cover_page.png)

---

### 📊 Correlation Heatmap

![Correlation Heatmap](images/correlation_heatmap.png)

---

### 📈 Model Performance Comparison

![Model Comparison](images/model_comparison.png)

---

### 🎯 Actual vs Predicted Deliveries

![Actual vs Predicted](images/actual_vs_predicted.png)

---

### 📉 Time Series Forecast

![Forecast](images/forecast_plot.png)











# 🎯 Objectives

- Perform Data Quality Assessment
- Clean and preprocess raw data
- Explore data using professional visualizations
- Engineer meaningful predictive features
- Build an End-to-End Machine Learning Pipeline
- Train multiple Regression Models
- Compare model performance
- Optimize the Random Forest model using Hyperparameter Tuning
- Forecast future Tesla deliveries
- Save the trained model for future deployment

---

# 📂 Repository Structure

```
Week2_Shreyash_Kedari_Dr_D_Y_Patil_Pimpri
│
├── README.md
├── WEEK_2_Shreyash_Kedari_Dr_D_Y_Patil_Pimpri.ipynb
├── Tesla_EV_Deliveries_Production.csv
└── tesla_delivery_prediction_model.pkl
```

---

# 🛠 Tech Stack

## Programming Language

- Python

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Seaborn

## Machine Learning

- Scikit-Learn

## Models Used

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

## Hyperparameter Optimization

- RandomizedSearchCV

## Time Series Forecasting

- Holt-Winters Exponential Smoothing

## Model Persistence

- Joblib

---

# 🔄 Machine Learning Workflow

```
Business Understanding
        │
        ▼
Data Collection
        │
        ▼
Data Quality Assessment
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Machine Learning Pipeline
        │
        ▼
Regression Modeling
        │
        ▼
Model Comparison
        │
        ▼
Hyperparameter Tuning
        │
        ▼
Time Series Forecasting
        │
        ▼
Model Persistence
```

---

# 📊 Exploratory Data Analysis

The dataset was explored using multiple visualizations including:

- Distribution Plots
- Correlation Heatmap
- Scatter Plot
- Line Charts
- Bar Charts
- Vehicle-wise Analysis
- Region-wise Analysis
- Delivery Trend Analysis

These visualizations helped understand feature relationships and guided model development.

---

# ⚙️ Feature Engineering

The following features were created to improve predictive performance:

- Quarter
- Season
- Price per Kilometer

Feature engineering enhanced the dataset by introducing meaningful business-oriented attributes.

---

# 🤖 Machine Learning Models

Three regression algorithms were trained and evaluated.

| Model | Purpose |
|--------|----------|
| Linear Regression | Baseline & Final Selected Model |
| Random Forest Regressor | Ensemble Learning |
| Gradient Boosting Regressor | Boosted Decision Trees |

Evaluation Metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

# 🏆 Model Performance

The models were compared using multiple regression metrics.

🏅 **Best Performing Model**

**Linear Regression**

Performance:

- **R² Score:** 0.9883
- **MAE:** 333.48
- **RMSE:** 411.94

The Linear Regression model achieved the highest predictive performance and was selected as the final deployment model.

---

# ⚡ Hyperparameter Tuning

RandomizedSearchCV was applied to optimize the Random Forest Regressor.

Optimized Parameters:

- Number of Trees
- Maximum Depth
- Minimum Samples Split
- Minimum Samples Leaf

Although the Random Forest model improved after tuning, Linear Regression continued to deliver the highest overall predictive accuracy.

---

# 📈 Time Series Forecasting

Future monthly Tesla deliveries were forecasted using the Holt-Winters Exponential Smoothing technique.

The notebook predicts delivery trends for the next **12 months**, providing insights for future demand planning and production estimation.

---

# 💾 Model Persistence

The final trained machine learning model was saved using **Joblib**.

```
tesla_delivery_prediction_model.pkl
```

This model can be directly loaded for inference without retraining.

---

# 💡 Business Insights

The analysis revealed several important insights:

- Production Units strongly influence vehicle deliveries.
- Battery Capacity and Vehicle Range exhibit a strong positive relationship.
- Linear Regression provides excellent predictive performance for this dataset.
- Tesla delivery trends remain relatively stable over time.
- Time series forecasting predicts consistent future deliveries.

---

# 🚀 Future Enhancements

Potential improvements include:

- XGBoost Regression
- LightGBM
- CatBoost
- Streamlit Dashboard
- Flask API Deployment
- Docker Containerization
- CI/CD Pipeline
- Cloud Deployment

---

# 📚 References

- Tesla Official Reports
- Scikit-Learn Documentation
- Pandas Documentation
- NumPy Documentation
- Matplotlib Documentation
- Seaborn Documentation
- Statsmodels Documentation

---

# 👨‍💻 Author

## Shreyash Kedari

🎓 Artificial Intelligence & Data Science

🏫 Dr. D. Y. Patil Institute of Technology, Pimpri

💼 Celebal Technologies Intern

---

<div align="center">

## ⭐ If you found this project helpful, consider giving it a Star!

### 🚀 Thank you for visiting this repository!

</div>
