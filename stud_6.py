import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create Student Dataset
data = pd.DataFrame({
    'Name': ['Arun', 'Bala', 'Cathy', 'David', 'Eva'],
    'StudyHours': [2, 4, 5, 6, 8],
    'Marks': [40, 55, 65, 80, 90]
})

# -------------------------------
# LINE PLOT
# -------------------------------

plt.plot(data['StudyHours'],
         data['Marks'],
         color='blue',
         marker='o',
         label='Marks')

# Labels and Title
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

# Legend
plt.legend()

# Annotation
plt.annotate('Highest Marks',
             xy=(8, 90),
             xytext=(6, 95),
             arrowprops=dict(facecolor='red'))

plt.show()

# -------------------------------
# SCATTER PLOT WITH ERROR BARS
# -------------------------------

# Error values
errors = [3, 4, 2, 5, 3]

plt.errorbar(data['StudyHours'],
             data['Marks'],
             yerr=errors,
             fmt='o',
             color='green',
             ecolor='red',
             capsize=5,
             label='Marks with Error')

# Labels and Title
plt.title("Scatter Plot with Error Bars")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

# Legend
plt.legend()

# Annotation
plt.annotate('Good Performance',
             xy=(6, 80),
             xytext=(4, 85),
             arrowprops=dict(facecolor='black'))

plt.show()

# -------------------------------
# INTERPRETATION
# -------------------------------

print("Interpretation:")
print("1. Students who study more hours generally score higher marks.")
print("2. The scatter plot shows a positive relationship between study hours and marks.")
print("3. Error bars represent variation in marks.")
