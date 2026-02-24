# Data Generation using Modelling and Simulation for Machine Learning

## 📖 Project Overview

This project demonstrates how simulation can be used to generate synthetic data for training Machine Learning models.

A queueing system was simulated using the Python simulation library **SimPy**.  
Random system parameters were generated and passed to the simulator to produce 1000 data samples.  
The generated dataset was then used to train and compare multiple Machine Learning regression models.

---

## 🎯 Objective

- To generate synthetic data using simulation
- To create 1000 simulation runs with random parameters
- To train and evaluate 8 ML models
- To compare performance using regression metrics
- To identify the best performing model

---

## 🛠 Simulation Tool Used

- **SimPy** – A process-based discrete-event simulation framework in Python.

Why SimPy?
- Lightweight
- Easy to integrate with ML
- Perfect for modeling queueing systems

---

## 🏦 Simulation Model: Queueing System

The system simulates a multi-server queue (like a bank or hospital system).

### 🔢 Input Parameters

| Parameter | Description | Lower Bound | Upper Bound |
|------------|-------------|-------------|-------------|
| arrival_rate | Customer arrival rate (λ) | 1 | 20 |
| service_rate | Service rate (μ) | 1 | 25 |
| num_servers | Number of servers | 1 | 5 |
| sim_time | Simulation duration | 200 | 1000 |

### 🎯 Output Variable

- Average Waiting Time (Target Variable)

---

## 🔁 Data Generation Process

1. Random parameters were generated within defined bounds.
2. Each parameter set was passed to the simulator.
3. The simulation was run for a fixed time.
4. Average waiting time was recorded.
5. Steps repeated 1000 times.

Final Dataset Size:
1000 rows × 5 columns


---

## 🤖 Machine Learning Models Used

The following regression models were trained:

1. Linear Regression  
2. Decision Tree Regressor  
3. Random Forest Regressor  
4. Gradient Boosting Regressor  
5. K-Nearest Neighbors (KNN)  
6. Support Vector Regressor (SVR)  
7. Multi-Layer Perceptron (Neural Network)  
8. XGBoost Regressor  

---

## 📊 Evaluation Metrics

Models were evaluated using:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## 📈 Results

| Model | MAE | RMSE | R² Score |
|--------|------|------|----------|
| Linear Regression | ... | ... | ... |
| Decision Tree | ... | ... | ... |
| Random Forest | ... | ... | ... |
| Gradient Boosting | ... | ... | ... |
| KNN | ... | ... | ... |
| SVR | ... | ... | ... |
| MLP | ... | ... | ... |
| XGBoost | ... | ... | ... |

👉 The best model was selected based on:
- Highest R² score
- Lowest RMSE

---

## 📊 Visualization

The following graphs were generated:

- Model comparison (R² Score)
- Feature importance plot
- Parameter vs waiting time analysis
- Residual analysis

---


---

## ⚙️ How to Run

1. Open the notebook in Google Colab.
2. Install required libraries:
pip install simpy xgboost
3. Run all cells.
4. Dataset will be generated automatically.
5. ML models will be trained and evaluated.

---

## 🔎 Key Observations

- Waiting time increases significantly when arrival rate exceeds service rate.
- Increasing number of servers reduces average waiting time.
- Tree-based ensemble models performed better than linear models.
- XGBoost / Random Forest achieved highest prediction accuracy.

---

## 📌 Conclusion

This project successfully demonstrates how simulation can be used as a powerful data generation technique for Machine Learning.

By integrating simulation with ML:
- We can create controlled synthetic datasets.
- Test model performance under various scenarios.
- Analyze system behavior efficiently.

The best performing model was __________ based on evaluation metrics.

---

## 🚀 Future Work

- Use hyperparameter tuning
- Increase simulation runs beyond 1000
- Use cross-validation
- Apply deep learning models
- Extend to real-world queue datasets

---

## 👩‍💻 Author

Saloni Singh  
