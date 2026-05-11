import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
data = pd.read_csv("C:/Users/acer/Documents/Salary_dataset.csv")

# 2. Simplified Frequency Analysis
# value_counts() does the work of np.unique and the for loop in one line
salary_counts = data['Salary'].value_counts().sort_index()

print("Frequency of Salaries:")
print(salary_counts)

# 3. Simplified Statistics
# You can get mean, median, etc., directly from the column
mean_salary = data['Salary'].mean()
median_salary = data['Salary'].median()
mode_salary = data['Salary'].mode()[0] # .mode() returns a Series, so we take the first value

print(f"\nMean Salary: {mean_salary}")
print(f"Median Salary: {median_salary}")
print(f"Mode Salary: {mode_salary}")

# 4. Variance and Std Dev
variance_salary = data['Salary'].var()
std_dev_salary = data['Salary'].std()

print(f"Variance: {variance_salary}")
print(f"Standard Deviation: {std_dev_salary}")

# 5. Visualizations
plt.figure(figsize=(12, 5))

sns.histplot(data['Salary'], bins=5, kde=True, color='skyblue')
plt.title("Salary Distribution")
plt.show()


sns.boxplot(x=data['Salary'], color='lightgreen')
plt.title("Box Plot of Salary")

plt.tight_layout()
plt.show()
