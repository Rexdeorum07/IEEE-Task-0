import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df= pd.read_csv("processed_student_performance.csv")

#This is just a time saver dictionary that I pasted everywhere to increase readability
label_format = dict(fontsize=15,family="Arial",fontweight="bold")

#Q1. Bar chart: Student names vs final scores:
plt.bar(df["Student"], df["Final_Score"], width= 0.4)
plt.xlabel("Student Name", **label_format)
plt.ylabel("Final Score", **label_format)
plt.title("Final Scores by Student", **label_format)
plt.xticks(rotation=90)
plt.yticks(np.arange(0,100,5))
plt.tight_layout()

plt.show()

#Q2. Scatter plot: Hours studied vs final score:
plt.scatter(df["Hours_Studied"], df["Final_Score"])
plt.xlabel("Hours Studied", **label_format)
plt.ylabel("Final Score", **label_format)
plt.title("Hours Studied vs Final Score", **label_format)
plt.xticks(np.arange(0,10,0.5))
plt.yticks(np.arange(0,100,5))

plt.show()

#Q3. Histogram: Distribution of final scores:
plt.hist(df["Final_Score"], bins=10, edgecolor="black")
plt.xlabel("Final Score", **label_format)
plt.ylabel("Number of Students", **label_format)
plt.title("Distribution of Final Scores", **label_format)
plt.xticks(np.arange(0,100,5))
plt.yticks(np.arange(0,32,2))

plt.show()

#Q4. One additional graph of your choice that shows an interesting relationship or pattern in the dataset:
# Here I have made a scatter plot showing the relation between attendance and the final scores
plt.scatter(df["Attendance"], df["Final_Score"])
plt.xlabel("Attendance", **label_format)
plt.ylabel("Final Score", **label_format)
plt.title("Attendance vs Final Score", **label_format)
plt.xticks(np.arange(0,100,5))
plt.yticks(np.arange(0,100,5))

plt.show()