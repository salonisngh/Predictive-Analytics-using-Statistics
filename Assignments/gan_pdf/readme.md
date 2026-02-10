# Learning Probability Density Functions using GAN (NO₂ Air Quality Data)

## Project Overview
This project aims to learn an unknown probability density function (PDF) of a transformed random variable using a Generative Adversarial Network (GAN).

The NO₂ concentration values from India's Air Quality dataset are transformed using a nonlinear function and a GAN is trained to learn the underlying data distribution directly from samples.

---

##  Objective
- Transform NO₂ feature into a new variable z
- Learn unknown distribution of z using GAN
- Generate synthetic samples
- Approximate probability density using KDE

---

## Dataset
- **Name:** India Air Quality Dataset
- **Source:** Kaggle
- **Feature Used:** NO₂ concentration

Dataset Link:  
https://www.kaggle.com/datasets/shrutibhargava94/india-air-quality-data


---

## Transformation Function

z = x + a_r * sin(b_r * x)

Where:

a_r = 0.5 * (r mod 7)
b_r = 0.3 * ((r mod 5) + 1)


r = My University Roll Number

---

##  GAN Architecture

### Learning Objective
- The transformed variable z is assumed to come from an unknown distribution.
- The GAN learns the probability distribution directly from z samples.
- No parametric distribution assumptions are made.

### Generator Input
Noise vector sampled from:
N(0,1)

### Generator
- Input: Noise vector ~ N(0,1)
- Dense(1 → 16) + ReLU
- Dense(16 → 32) + ReLU
- Dense(32 → 1)

### Discriminator
- Dense(1 → 32) + ReLU
- Dense(32 → 16) + ReLU
- Dense(16 → 1) + Sigmoid

Function:
- Distinguish between real z samples and generated samples.

##  PDF Approximation

After training:

1. Generate a large number of samples from the generator.
2. Estimate probability density using Kernel Density Estimation (KDE).
3. Compare real and generated distributions.
---
## Learned Probability Density Function

<img width="699" height="451" alt="plot" src="https://github.com/user-attachments/assets/ff061755-b238-44c3-b7d2-e66c1398e58b" />


---
##  Methodology

1. Load NO₂ data
2. Apply nonlinear transformation
3. Normalize transformed values
4. Train GAN using only samples of z
5. Generate synthetic samples
6. Estimate PDF using Kernel Density Estimation (KDE)

---

##  Output
- Generated synthetic samples
- GAN learned probability density
- Histogram vs KDE plot

---

##  Observations

### Mode Coverage
GAN captures major distribution modes but minor modes may be smoothed.

### Training Stability
Stable training achieved using normalized data and Adam optimizer.

### Distribution Quality
Generated samples closely match the real transformed data distribution.

---

## Tech Stack
- Python
- PyTorch
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

---

## How to Run

### Install Dependencies
pip install pandas numpy matplotlib torch scikit-learn

### Run Script
python gan_pdf_learning.py

---

### Author
Saloni




