# IEEE Task 0

This repository contains my submission for Task 0 of the IEEE Club at BITS Pilani, Pilani Campus.

The project consists of six Python programs covering basic Python programming, functions, NumPy, Pandas, data processing, and data visualization.

## 1. Requirements:
To run this project, you need:
-Python 3
-NumPy
-Pandas
-Matplotlib


## 2. Install Dependencies

-Install all required Python libraries:
-pip install numpy pandas matplotlib
-After installation, the project is ready to run.

## 3. Running the Programs
-All Python files should be run from the root directory of the repository.

### Question 1 — Basic List Operations

Run:

python task0_Q1.py

The program asks the user to enter:

The number of elements.
Each number individually.

It then performs operations such as:

Displaying the entered list.
Finding the largest element.
Finding the smallest element.
Calculating the sum of all elements.
Counting even numbers.
Counting odd numbers.
Printing the list in reverse order.
Example
Enter the count of your numbers: 5
Enter number 1: 10
Enter number 2: 7
Enter number 3: 4
Enter number 4: 15
Enter number 5: 8

### Question 2 — Processing a List

Run:

python task0_Q2.py

The program:

Takes a list of integers from the user.
Removes negative numbers from a copy of the list.
Adds 0 to the resulting list.
Sorts the resulting list.

The original list remains unchanged.

### Question 3 — Prime Number Checker

Run:

python task0_Q3.py

The program:

Takes an integer from the user.
Checks whether the number is prime.
Prints all prime numbers from 2 up to the entered number.
Example
Enter the number you want to test: 10

The program will display whether 10 is prime and list the prime numbers up to 10.

### Question 4 — NumPy Operations

Run:

python task0_Q4.py

This program uses NumPy arrays containing example student data.

It performs operations including:

Displaying array shapes and data types.
Calculating the mean final score.
Finding maximum and minimum scores.
Calculating the standard deviation.
Adding bonus marks to all final scores.
Using Boolean indexing to identify students meeting a score condition.
Dependency Required
pip install numpy

### Question 5 — Pandas Data Analysis

Run:

python task0_Q5.py

This program reads data from:

student_performance.csv

It performs several operations using Pandas, including:

Loading the CSV dataset.
Displaying the first five rows.
Finding the number of rows and columns.
Displaying column names.
Checking for missing values.
Calculating the average final score.
Finding the student with the highest final score.
Creating an Improvement column.
Filtering students based on attendance.
Sorting students by final score.
Saving the processed data.

The processed dataset is saved as:

processed_student_performance.csv

### Question 6 — Data Visualization

Run:

python task0_Q6.py

This program reads:

processed_student_performance.csv

and generates the following visualizations:

-Bar chart of student names vs final scores.
-Scatter plot of hours studied vs final score.
-Histogram showing the distribution of final scores.
-Scatter plot showing attendance vs final score.

The graphs are displayed using Matplotlib.

Important

The file:

processed_student_performance.csv

must be present before running this program.

If the file is missing, first run:

python task0_Q5.py

This will generate the required processed CSV file.

Dependencies Required
pip install numpy pandas matplotlib

## Recommended Order of Execution

Although most programs can be run independently, the recommended order is:

task0_Q1.py
     ↓
task0_Q2.py
     ↓
task0_Q3.py
     ↓
task0_Q4.py
     ↓
task0_Q5.py
     ↓
task0_Q6.py

The most important dependency is:

student_performance.csv
        ↓
   task0_Q5.py
        ↓
processed_student_performance.csv
        ↓
   task0_Q6.py

Therefore, if you want to run the complete data analysis and visualization workflow, run:

python task0_Q5.py
python task0_Q6.py
Quick Start


## Author Info
Shubh Gupta
BITS ID: 2026A7UB1757P
Submission for IEEE Task 0
IEEE Club, BITS Pilani, Pilani Campus.
