# Curve Fitting for Landslide Susceptibility Prediction

##  Overview
This repository contains the Python script and dataset used to develop a mathematical model for predicting landslide susceptibility using curve fitting. The method involves fitting a custom equation to estimate landslide susceptibility based on specific conditioning parameters. This approach is a type of  regression, which models the relationship between the input variables and landslide susceptibility.

##  Methodology
### **Defined Variables**
- **x₁** = Class number of the conditioning parameter (e.g., slope class, lithology class).
- **x₂** = Total number of pixels in the study area.
- **y** = Total number of pixels in the training landslides area.

### **Mathematical Model**
The relationship between the variables is modeled using the following equation:

y = a * x₁⁴ + b * ln(x₂) + c * x₁ + d * x₁

Where:
- **a, b, c, d** are the parameters estimated through non-linear least squares fitting.
- **ln(x₂)** is the natural logarithm of **x₂**.

### **Implementation**
- We used Python's **SciPy** library to perform curve fitting with the `curve_fit` function from `scipy.optimize`.
- The estimated parameters were used to generate a **Landslide Susceptibility Index (LSI)** map.
- The LSI values were classified into five categories: **Very High, High, Moderate, Low, and Very Low Susceptibility.**
- The high LSI values indicate areas with a higher likelihood of landslides.

##  Files in This Repository
- `curve_fitting.py` → Python script implementing the curve fitting method.
- `Dataset.xlsx` → Dataset used.

##  How to Run the Script
### **1. Install Dependencies**
Make sure you have Python installed. Then install required libraries:
```bash
pip install numpy scipy
```

### **2. Run the Script**
Execute the script using:
```bash
python curve_fitting.py
```

##  Output
- The script estimates parameters for the mathematical model.
- Outputs the predicted vs actual values.
- The results can be used for generating landslide susceptibility maps.


