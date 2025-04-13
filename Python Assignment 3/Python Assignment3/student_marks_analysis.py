import pandas as pd

# Load the CSV file
df = pd.read_csv("student_marks.csv")

# Display the first few rows
print("Student Marks Data:")
print(df)

# Calculate average marks per student
avg_marks = df.groupby("Name")["Marks"].mean()
print("\nAverage Marks per Student:")
print(avg_marks)

# Find the top scorer overall
total_marks = df.groupby("Name")["Marks"].sum()
top_scorer = total_marks.idxmax()
print(f"\nTop Scorer: {top_scorer} with {total_marks[top_scorer]} total marks")

# Optional: Average marks by subject
avg_by_subject = df.groupby("Subject")["Marks"].mean()
print("\nAverage Marks by Subject:")
print(avg_by_subject)
