
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("students_data.csv")

print(df.head())
print(df.tail())
print(df.info())

print(df.describe())

df["Score_per_Hour"] = np.round(df["Score"] / df["Hours_Studied"], 2)

filtered = df[df["Score"] > 75]
filtered.to_csv("filtered_students.csv", index=False)

sns.histplot(df["Score"], kde=True)
plt.title("Score Distribution")
plt.show()

sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

plt.plot(df["Student_ID"], df["Score"])
plt.title("Scores Trend")
plt.xlabel("Student ID")
plt.ylabel("Score")
plt.show()

print(f"Total Records: {len(df)}")
print("High performing students saved to filtered_students.csv")
