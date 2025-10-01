import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats

dataset = [5, 12, 15, 8, 9, 11, 15, 17, 10, 15]

print("Mean:", np.mean(dataset))
print("Median:", np.median(dataset))
print("Mode:", stats.mode(dataset, keepdims=True))

print("Standard Deviation:", np.std(dataset))

print("25th Percentile:", np.percentile(dataset, 25))
print("50th Percentile:", np.percentile(dataset, 50))
print("75th Percentile:", np.percentile(dataset, 75))