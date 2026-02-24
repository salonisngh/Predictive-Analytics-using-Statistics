# Data Generation using Modelling and Simulation for Machine Learning

## 📌 Assignment Overview

This project demonstrates how modelling and simulation can be used to generate synthetic data for Machine Learning tasks.

A queueing system was simulated using the Python-based discrete-event simulation library **SimPy**. Random parameter sets were generated and passed into the simulator to produce 1000 simulation samples. The generated dataset was then used to train and compare multiple Machine Learning regression models.

---

# ✅ Step 1: Selection of Simulation Tool

### Simulation Tool Chosen: SimPy

SimPy is a process-based discrete-event simulation framework in Python.

### Why SimPy?
- Lightweight and easy to install
- Works well with Google Colab
- Easy integration with ML libraries
- Suitable for queueing system modelling

---

# ✅ Step 2: Installation and Exploration

The following libraries were installed:

Key SimPy components explored:
- Environment
- Resource (Server)
- Process
- Timeout
- Event scheduling

---

# ✅ Step 3: Important Parameters and Bounds

The system simulated a multi-server queue (similar to a bank or hospital system).

## Input Parameters and Bounds

| Parameter | Description | Lower Bound | Upper Bound |
|------------|-------------|-------------|-------------|
| arrival_rate (λ) | Rate of customer arrivals | 1 | 20 |
| service_rate (μ) | Rate of service completion | 1 | 25 |
| num_servers | Number of parallel servers | 1 | 5 |
| sim_time | Total simulation duration | 200 | 1000 |

## Output Variable (Target)

- Average Waiting Time of customers

---

# ✅ Step 4: Random Parameter Generation & Simulation

For each simulation run:
1. Random values were generated within defined bounds.
2. These values were passed to the simulator.
3. The simulation ran for the specified time.
4. The average waiting time was recorded.

This process created one data sample per simulation.

---

# ✅ Step 5: 1000 Simulation Runs

The simulation process was repeated 1000 times.

Final dataset:

- 1000 rows
- 4 input features
- 1 target variable

Dataset structure:

| arrival_rate | service_rate | num_servers | sim_time | avg_wait_time |
|--------------|-------------|-------------|----------|---------------|

The dataset was saved as:
simulation_dataset.csv


---

# ✅ Step 6: Machine Learning Model Comparison

The generated dataset was split into training and testing sets (80-20 split).

## ML Models Used

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. Gradient Boosting Regressor
5. K-Nearest Neighbors (KNN)
6. Support Vector Regressor (SVR)
7. Multi-Layer Perceptron (Neural Network)
8. XGBoost Regressor

---

# 📊 Evaluation Metrics

Models were evaluated using:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

# 📈 Results Comparison Table

The following table shows the performance of all 8 regression models:

| Model | MAE | RMSE | R² Score |
|--------|--------|--------|----------|
| XGBoost | 10.67 | 24.73 | 0.8806 |
| MLP | 16.32 | 28.82 | 0.8378 |
| Random Forest | 13.68 | 31.36 | 0.8079 |
| Decision Tree | 13.73 | 37.77 | 0.7213 |
| Gradient Boosting | 20.81 | 40.44 | 0.6806 |
| Linear Regression | 37.82 | 55.87 | 0.3904 |
| KNN | 28.67 | 61.39 | 0.2639 |
| SVR | 28.84 | 77.09 | -0.1607 |


# 🏆 Best Performing Model

The best-performing model is **XGBoost**, based on:

- Highest R² Score (0.8806)
- Lowest RMSE (24.73)
- Lowest MAE (10.67)

This indicates that XGBoost was able to capture the non-linear relationships in the simulated queueing system more effectively than other models.

---

# 🔎 Analysis of Results

- Ensemble models (XGBoost, Random Forest) performed significantly better than simple linear models.
- Linear Regression performed poorly because the system behavior is non-linear.
- SVR showed negative R² score, indicating poor generalization on this dataset.
- Neural Network (MLP) performed well but slightly below XGBoost.
- Tree-based methods handled parameter interactions effectively.

---

# 🎯 Final Conclusion

This project successfully demonstrates that simulation-generated data can be effectively used for Machine Learning tasks.

The queueing system exhibited non-linear behaviour, and ensemble models like XGBoost were best suited to capture these patterns.

Therefore, XGBoost is selected as the final model for predicting average waiting time in the simulated system.

---

# 🚀 Future Improvements

- Hyperparameter tuning
- Cross-validation
- Increasing simulations beyond 1000
- Applying deep learning models
- Using real-world queue datasets for validation

---

# 👩‍💻 Author

Saloni Singh  
B.Tech Student  


