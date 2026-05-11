# Create Dataset
student_data <- data.frame(
  Student = c("A", "B", "C", "D", "E"),
  Marks = c(80, 60, 75, 90, 50),
  Age = c(20, 21, 19, 22, 20)
)



# View dataset
print(student_data)

# Filter Rows
high_marks <- student_data[student_data$Marks > 70, ]
print(high_marks)

# Histogram
hist(student_data$Marks,
     main="Histogram of Marks",
     xlab="Marks",
     col="lightblue")

# Boxplot
boxplot(student_data$Marks,
        main="Boxplot of Marks",
        ylab="Marks",
        col="lightgreen")

# Barplot
barplot(student_data$Marks,
        names.arg=student_data$Student,
        main="Bar Plot of Marks",
    
        xlab="Students",
        ylab="Marks",
        col="lightcoral")

# Scatter Plot
plot(student_data$Age,
     student_data$Marks,
     main="Scatter Plot: Age vs Marks",
     xlab="Age",
     ylab="Marks",
     col="blue",
     pch=19)

