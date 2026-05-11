# -------------------------------
# Part 1: Import Libraries
# -------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Part 2: Load Dataset
# -------------------------------
data = pd.read_csv("C:/Users/acer/Documents/New folder/WineQT.csv")

print("First 5 rows of dataset:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nSummary Statistics:")
print(data.describe())

# -------------------------------
# Part 3: Check for Missing Values
# -------------------------------
print("\nMissing Values:")
print(data.isnull().sum())

# -------------------------------
# Part 4: Visualizations
# -------------------------------

# Histogram of features (excluding Id column)
data.drop('Id', axis=1).hist(figsize=(12,10), bins=15, color='skyblue')
plt.suptitle("Feature Distributions")
plt.show()

# Boxplot: Alcohol vs Quality
plt.figure(figsize=(6,4))
sns.boxplot(x='quality', y='alcohol', data=data)
plt.title('Alcohol vs Quality')
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12,8))
col = ['alcohol' , 'quality', 'density','citric acid','chlorides']
sns.heatmap(data[col].corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Scatter plot: Alcohol vs Density colored by Quality
plt.figure(figsize=(6,4))
sns.scatterplot(x=data['alcohol'], y=data['quality'],hue=data['density'])
plt.title('Alcohol vs Density by Quality')
plt.show()

sns.countplot(x=data['quality'], data= data)
plt.title("Wine quality distribution")
plt.show()

sns.kdeplot(data['alcohol'], shade= True)
plt.title("Density plot of alcohol content")
plt.show()

