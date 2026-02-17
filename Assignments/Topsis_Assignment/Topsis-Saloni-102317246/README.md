# Topsis-Saloni-102317246

**Project-1 (UCS633)**  
Submitted by: Saloni Singh  
Roll No: 102317246  

---

##  Description

`Topsis-Saloni-102317246` is a Python library for solving **Multiple Criteria Decision Making (MCDM)** problems using the **Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)** method.

The package takes a CSV file as input along with weights and impacts vectors, and produces TOPSIS performance scores and rankings.

---

##  Installation

Use pip to install the package:

```bash
pip install Topsis-Saloni-102317246
```

---
## Usage

Enter:

1.CSV filename (with .csv extension)

2.Weights vector (comma-separated values)

3.Impacts vector (comma-separated signs + or -)

---

## Format:
```bash
topsis <inputfile.csv> <weights> <impacts>
```
Example:
```bash
topsis sample.csv "1,1,1,1" "+,-,+,+"
```

OR
```bash
topsis sample.csv 1,1,1,1 +,-,+,+
```

⚠️ If vectors contain spaces, enclose them in double quotes (" ").

To view usage help:
```bash
topsis /h
```

---
## Example

sample.csv

A CSV file containing data for different mobile handsets with various features:

| Model | Storage (GB) | Camera (MP) | Price ($) | Looks (out of 5) |
| ----- | ------------ | ----------- | --------- | ---------------- |
| M1    | 16           | 12          | 250       | 5                |
| M2    | 16           | 8           | 200       | 3                |
| M3    | 32           | 16          | 300       | 4                |
| M4    | 32           | 8           | 275       | 4                |
| M5    | 16           | 16          | 225       | 2                |

Weights Vector: 
0.25,0.25,0.25,0.25

Impacts Vector: 
+,+,-,+

Input:
topsis sample.csv "0.25,0.25,0.25,0.25" "+,+,-,+"

Output:

## TOPSIS RESULTS
-----------------------------

    P-Score   | Rank
-----------------------------
1 | 0.534277  |  3

2 | 0.308368  |  5

3 | 0.691632  |  1

4 | 0.534737  |  2

5 | 0.401046  |  4



⚠️ Notes

The first column and first row are removed automatically to handle indices and headers.

The CSV must contain only numeric values (except the first column).

The number of weights and impacts must match the number of criteria columns


## LICENESE 
MIT



