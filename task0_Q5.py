import pandas as pd

#Q1. Loading the CSV into a DataFrame:
df= pd.read_csv("student_performance.csv")

#Q2. Printing first 5 rows:
print("Q2: The first 5 rows are: \n\n", df.loc[0:4])
print("\n")

#Q3. Printing the number of rows and columns:
print("Q3: The number of rows and columns are: \n", df.shape)
print("\n")

#Q4. Displaying the column names:
print("Q4: The column names are: \n", df.columns.tolist())
print("\n")

#Q5. Checking if the dataset has missing values:
print("Q5: The data has missing values = ", df.isnull().values.any())
print("\n")

#Q6. Calculating average final score:
print("Q6: The average final score is: \n", df["Final_Score"].mean())
print("\n")

#Q7. Finding Student with highest final score:
max_index = df["Final_Score"].idxmax()
print("Q7: The student with the highest final score is: ", df.loc[max_index, "Student"])
print("\n")

#Q8. Creating a new column named "Improvement":
df["Improvement"] = df["Final_Score"] - df["Previous_Score"]
print("Q8: The data set after adding a new column named 'Improvement': \n\n",df)
print("\n")

#Q9. Displaying only students with attendance greater than or equal to 80:
print("Q9: The info of students having attendance greater than or equal to 80: \n")
print(df[df["Attendance"] >= 80].to_string())
print("\n")

#Q10. Sorting the DataFrame by Final_Score in descending order:
print("Q10: The dataset after sorting it by descendeing order of final scores: \n")
sorted_df = df.sort_values("Final_Score", ascending=False)
print(sorted_df)
print("\n")

#Q11. Saving the processed DataFrame as "processed_student_performance.csv":
sorted_df.to_csv("processed_student_performance.csv")






