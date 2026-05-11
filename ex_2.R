# -----------------------------------
# Student Performance Dataset
# -----------------------------------


student <- data.frame(
  Name = c("A", "B", "C", "D", "E"),
  Marks = c(85, 40, 75, 90, 35),
  Attendance = c(95, 60, 80, 98, 50),
  Grade = c("A", "D", "B", "A", "F")
)

print("Original Dataset")
print(student)

# -----------------------------------
# Row Filtering for Data Cleaning
# Remove students with Marks < 40
# -----------------------------------

clean_data <- subset(student, Marks >= 40)

print("Cleaned Dataset")
print(clean_data)

# -----------------------------------
# Scatter Plot
# -----------------------------------

plot(clean_data$Attendance,
     clean_data$Marks,
     main = "Attendance vs Marks",
     xlab = "Attendance",
     ylab = "Marks",
     col = "blue",
     pch = 19)

# Add text labels
text(clean_data$Attendance,
     clean_data$Marks,
     labels = clean_data$Name,
     pos = 4)

# -----------------------------------
# Bar Plot
# -----------------------------------

barplot(clean_data$Marks,
        names.arg = clean_data$Name,
        col = "green",
        main = "Student Marks",
        xlab = "Students",
        ylab = "Marks")

# -----------------------------------
# Line Plot
# -----------------------------------

plot(clean_data$Marks,
     type = "o",
     col = "red",
     main = "Marks Trend",
     xlab = "Student Index",
     ylab = "Marks")

# -----------------------------------
# Pie Chart
# -----------------------------------

grade_count <- table(clean_data$Grade)

pie(grade_count,
    main = "Grade Distribution",
    col = rainbow(length(grade_count)))

# -----------------------------------
# Interpretation
# -----------------------------------

print("Interpretation:")
print("1. Students with low marks were removed during cleaning.")
print("2. Higher attendance leads to better marks.")
print("3. Most students scored Grade A and B.")
print("4. Scatter plot shows positive relationship.")

