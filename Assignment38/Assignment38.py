'''
Q1. Write a Python program to load the file student_performance_ml.csv using pandas. 
Display:
First 5 records
Last 5 records
Total number of rows and columns
List of column names
Data types of each colums

'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load csv

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

# first 5 records
print("First 5 records\n")
print(df.head())

# last 5 records
print("last 5 records\n")
print(df.tail())

#Total number of rows and columns
rows,cols = df.shape

print("\ntotal rows = ",rows)
print("\ntotal columns = ",cols)

#List of column names

print("\nColumn names = ")
print(list(df.columns))

#Data types of each columns
print("\nData types of each columns =")
print(df.dtypes)

'''
Q2. write a program to:
Display total number of students in the dataset
Count how many students Passed(FinalResult = 1)
Count how many students Failed (FinalResult = 0)

'''

# Total number of students
total_students = len(df)
print("Total Students:", total_students)

#Count how many students Passed(FinalResult = 1)
passed = (df["FinalResult"]==1).sum()
print("Passed Students = ",passed)

#Count how many students Failed (FinalResult = 0)
failed = (df["FinalResult"]==0).sum()
print("Failed = ",failed)

'''
Q3. Using pandas functions, calculate and display:
Average StudyHours
Average Attendance
Maximum PreviousScore
Minimum SleepHours

'''
#Average StudyHours
average_studyHours = df["StudyHours"].mean()
print("Average Study Hours = ",average_studyHours)

#Average Attendance
average_attendance = df["Attendance"].mean()
print("Average Attandance = ",average_attendance)

#Maximum PreviousScore
Maximum_PreviousScore = df["PreviousScore"].max()
print("Maximum PreviousScore = ",Maximum_PreviousScore)

#Minimum SleepHours
Minimum_SleepHours = df["SleepHours"].min()
print("Minimum SleepHours = ",Minimum_SleepHours)

'''
Q4.Use value_counts() to analyse the distribution of FinalResult.
Calculate the percentage of pass and fail students.
Is the Dataset balanced? justify your answer
'''
#Count pass and fail.
counts = df["FinalResult"].value_counts()
print("Distribution of final result: \n",counts)

#percentage of pass and fail
percentage = df["FinalResult"].value_counts(normalize=True)*100
print("percentage of pass and fail = ",percentage)

'''
Q6. Plot a histogram of StudyHours.
Explain what the Distribution tells you.
'''
histogram = sns.histplot(df["StudyHours"],bins=10,kde=True)

plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")

plt.show()

'''
Q7.Create a Scatter Plot of:
StudyHours vs PreviousScore
'''
sns.scatterplot(
    x="StudyHours",
    y="PreviousScore",
    hue="FinalResult",   
    data=df
)

plt.title("Study Hours vs Previous Score (Pass/Fail)")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")

plt.show()

'''
Q8. Draw a boxplot for Attendance.
Identify if any outliers are present.
'''
sns.boxplot(y=df["Attendance"])

plt.title("Boxplot of Attendance")
plt.ylabel("Attendance")

plt.show()

'''
Q9. Create a plot showing relationship between AssignmentCompleted and FinalResult.
Explain your observation.
'''
sns.countplot(x="AssignmentsCompleted", hue="FinalResult", data=df)

plt.title("Assignment Completed vs Final Result")
plt.xlabel("Assignment Completed")
plt.ylabel("Number of Students")

plt.show()

'''
Q10. Plot SleepHours Against FinalResult.
Does sleeping more guarentee success? Explain.
'''

df["ResultLabel"] = df["FinalResult"].map({0: "Fail", 1: "Pass"})

sns.boxplot(x="ResultLabel", y="SleepHours", data=df)

plt.title("Sleep Hours vs Final Result")
plt.xlabel("Final Result")
plt.ylabel("Sleep Hours")

plt.show()