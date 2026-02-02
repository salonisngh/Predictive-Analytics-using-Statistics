# Learning Probability Density Functions using NO₂ Data

## Assignment Title
Learn Probability Density Functions using Roll-Number-Parameterized Non-Linear Model

---

## Dataset
- **Name:** India Air Quality Dataset
- **Source:** Kaggle
- **Feature Used:** NO₂ concentration

Dataset Link:  
https://www.kaggle.com/datasets/shrutibhargava94/india-air-quality-data

---

## Objective
The objective of this assignment is to apply a roll-number-dependent non-linear
transformation on NO₂ data and learn a probability density function (PDF) for
the transformed variable.

---

## Step 1: Non-Linear Transformation
Each NO₂ value `x` is transformed into `z` using the following function:

```
z = x + aᵣ sin(bᵣ x)
```

Where:
- aᵣ = 0.05 × (r mod 7)
- bᵣ = 0.3 × (r mod 5 + 1)
- r is the University Roll Number

This transformation introduces non-linearity and ensures a unique transformation
for each student.

---

## Step 2: Probability Density Function Learning
The transformed variable `z` is modeled using the following probability density
function:

```
p̂(z) = c · exp(−λ (z − μ)²)
```

### Parameter Estimation
The parameters are learned using **Maximum Likelihood Estimation (MLE)**:
- **μ**: Mean of the transformed data  
- **λ**: Spread (inverse variance) parameter  
- **c**: Normalization constant ensuring the PDF integrates to 1  

---

## How to Run
1. Install required libraries:
```
pip install numpy pandas 
```

2. Run the Python script:
```
python UCS654_Assignment01.ipynb
```

---

## Output
- Printed values of **μ, λ, and c**
- Histogram of transformed NO₂ data with learned PDF curve

---

## Learning Outcomes
- Understanding roll-number-based non-linear transformations  
- Learning probability density functions from real-world data  
- Applying Maximum Likelihood Estimation  
- Visual validation of probabilistic models  

---

## Author
Saloni Singh  

