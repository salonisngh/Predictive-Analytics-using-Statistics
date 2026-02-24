# TOPSIS-Based Selection of Best Pre-Trained Text Generation Model

##   Objective

The objective of this project is to apply the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** multi-criteria decision-making method to identify the best pre-trained model for **Text Generation**.

---

##   Models Compared

The following popular pre-trained text generation models were evaluated:

1. GPT-2  
2. LLaMA 2  
3. T5  
4. GPT-Neo  
5. BLOOM  

---

##   Evaluation Criteria

The models were compared using the following criteria:

| Criteria      | Type     | Description |
|--------------|----------|------------|
| BLEU Score   | Benefit  | Measures text generation quality |
| ROUGE Score  | Benefit  | Measures overlap similarity |
| Perplexity   | Cost     | Lower indicates better fluency |
| Inference Time | Cost   | Model speed |
| Model Size   | Cost     | Deployment feasibility |

---

##   Weights Assigned

The following weights were assigned based on importance:

- BLEU → 0.25  
- ROUGE → 0.25  
- Perplexity → 0.20  
- Time → 0.15  
- Size → 0.15  

(Sum of weights = 1)

---

##   Methodology (TOPSIS Steps)

1. Construct Decision Matrix  
2. Normalize the Matrix  
3. Multiply by Weights  
4. Determine Ideal Best and Ideal Worst  
5. Compute Distance from Ideal Solutions  
6. Calculate Closeness Coefficient  
7. Rank Models  

---

##  Results

After applying TOPSIS, the models were ranked based on their Closeness Coefficient.

| Rank | Model     |
|------|----------|
| 1    | LLaMA 2  |
| 2    | T5       |
| 3    | BLOOM    |
| 4    | GPT-2    |
| 5    | GPT-Neo  |

---

## Conclusion

Based on the TOPSIS analysis, **LLaMA 2** achieved the highest closeness coefficient, indicating the best balance between performance quality and computational efficiency.  

Therefore, LLaMA 2 is selected as the optimal pre-trained model for text generation among the evaluated alternatives.


---

## Technologies Used

- Python  
- NumPy  
- Pandas  
- Matplotlib  

---

##  Author

Saloni Singh  
B.Tech Student  

