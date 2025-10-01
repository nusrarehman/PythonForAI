
import matplotlib.pyplot as plt
import pandas as pd

# DataFrame
students = {
    "Name": ["Danyal", "Arham", "Moosa", "Haseeb", "Hanzla"],
    "Age": [22, 25, 28, 23, 26],
    "Marks": [92, 90, 95, 88, 90]
}
df = pd.DataFrame(students)

# Create figure with 2 plots (1 row, 2 columns)
plt.figure(figsize=(10,4))


plt.subplot(1, 2, 1)
plt.bar(df["Name"], df["Marks"], color="orange", edgecolor="black")
plt.title("Student Performance")
plt.xlabel("Names")
plt.ylabel("Marks")


plt.subplot(1, 2, 2)
plt.plot(df["Age"], df["Marks"], marker="o", color="blue", linestyle="--")
plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.grid(True)


plt.tight_layout()
plt.show()