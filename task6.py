import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats
import seaborn as sns
import pandas as pd

data = {
    "Age": [18, 19, 20, 21, 22, 23, 24],
    "Marks": [55, 65, 75, 80, 60, 85, 90],
    "Grade": ["C", "B", "A", "A", "B", "A", "A"]
}
df = pd.DataFrame(data)


sns.boxplot(y="Marks", data=df, color="lightblue")
plt.title("Marks Boxplot")
plt.show()

sns.violinplot(x="Grade", y="Marks", data=df, inner="quartile", palette="muted")
plt.title("Marks Distribution by Grade")
plt.show()


sns.heatmap(df[["Age","Marks"]].corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()