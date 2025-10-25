import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("rainfall.csv")
print("Rainfall statistics:")
print(data.describe())

plt.figure(figsize=(10,6))
sns.barplot(x='Month', y='Rainfall_mm', data=data, palette='Blues_d')
plt.title('Monthly Rainfall')
plt.ylabel('Rainfall (mm)')
plt.show()

plt.figure(figsize=(10,6))
sns.lineplot(x='Month', y='Rainfall_mm', data=data, marker='o')
plt.title('Rainfall Trend')
plt.ylabel('Rainfall (mm)')
plt.show()
