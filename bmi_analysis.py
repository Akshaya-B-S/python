import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv("C:/Users/acer/Downloads/BMI.csv")

# --- BASIC ANALYSIS ---
print("--- Average Metrics by Gender ---")
print(df.groupby('Gender')[['Age', 'Weight', 'BMI', 'Heart Rate']].mean())

print("\n--- Health Risk Counts ---")
print(df['Health Risk Level'].value_counts())

gender_bmi= pd.crosstab(df['Gender'], df['Age'])
print("--- Gender vs. bmiclass ---")
print(gender_bmi)

# --- VISUALIZATIONS ---

# 1. Count Plot: Patients vs Health Risk
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='BmiClass')
plt.title("Number of Patients per Age")
plt.show()

# 2. Scatter Plot: Height vs Weight (Colored by Health Risk)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df.head(50), x='Height', y='Weight', hue='BmiClass', s=100)
plt.title("Height vs Weight Relationship")
plt.show()

# 3. 3D-Style Scatter (using Bubble Size): Age, Height, and Weight
# We use Age for the X-axis, Weight for the Y-axis, and Height for the SIZE of the dots
plt.figure(figsize=(12, 6))
col = ['Age','Height','Weight']
sns.heatmap(data=df[col].corr(), annot=True)
plt.title("Relationship between Age, Weight, and Height (Bubble Chart)")

plt.show()
