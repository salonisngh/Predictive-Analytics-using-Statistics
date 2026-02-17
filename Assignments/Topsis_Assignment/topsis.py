import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):

    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit()

    if data.shape[1] < 3:
        print("Error: Input file must contain three or more columns.")
        sys.exit()

    decision_matrix = data.iloc[:, 1:]

    if not np.issubdtype(decision_matrix.values.dtype, np.number):
        print("Error: From 2nd to last columns must contain numeric values only.")
        sys.exit()

    weights = weights.split(',')
    impacts = impacts.split(',')

    if len(weights) != len(impacts) or len(weights) != decision_matrix.shape[1]:
        print("Error: Number of weights, impacts and columns must be same.")
        sys.exit()

    weights = np.array(weights, dtype=float)

    for impact in impacts:
        if impact not in ['+', '-']:
            print("Error: Impacts must be either '+' or '-'.")
            sys.exit()

    norm_matrix = decision_matrix / np.sqrt((decision_matrix**2).sum())
    weighted_matrix = norm_matrix * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted_matrix.iloc[:, i].max())
            ideal_worst.append(weighted_matrix.iloc[:, i].min())
        else:
            ideal_best.append(weighted_matrix.iloc[:, i].min())
            ideal_worst.append(weighted_matrix.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    s_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
    s_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))

    score = s_worst / (s_best + s_worst)

    data['Topsis Score'] = score
    data['Rank'] = data['Topsis Score'].rank(method='max', ascending=False)

    data.to_csv(output_file, index=False)
    print("Result successfully written to", output_file)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <InputFile> <Weights> <Impacts> <OutputFile>")
        sys.exit()

    _, input_file, weights, impacts, output_file = sys.argv
    topsis(input_file, weights, impacts, output_file)
