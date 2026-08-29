import numpy as np

#*******************<example data>**********************

names=np.array(['Aarav','Diya', 'Kabir', 'Meera', 'Rohan', 'Ananya'])
hours_studied=np.array([5.9, 3.6, 6.5, 5.4, 1.2, 7.3])
attendance=np.array([100, 85, 73, 73, 74, 92])
previous_scores=np.array([52, 74, 49, 78, 77, 49])
final_scores=np.array([60, 78, 41, 92, 85, 69])


#Q1-Printing array shape and dataype:
print("Q1:")
print("Array Name: names ",",","Array Shape: ", names.shape ,",", "Array Data Type: ", names.dtype )
print("Array Name: hours studied ",",","Array Shape: ", hours_studied.shape ,"," "Array Data Type: ", hours_studied.dtype )
print("Array Name: attendance ",",","Array Shape: ", attendance.shape ,",", "Array Data Type: ", attendance.dtype)
print("Array Name: previous scores ",",","Array Shape: ",previous_scores.shape ,",", "Array Data Type: ", previous_scores.dtype )
print("Array Name: final scores ",",","Array Shape: ", final_scores.shape,",", "Array Data Type: ", final_scores.dtype)
print("\n")

#Q2-Finding mean final score:
mean=np.sum(final_scores)/6
print("Q2: The mean final score is: ", mean)
print("\n")


#Q3-Finding the minimum and maximum scores:
print("Q3:")
print("The maximum final score is: ", np.max(final_scores))
print("The minimum final score is: ", np.min(final_scores))
print("\n")


#Q4-Finding the standard deviation of final scores:
print("Q4: The standard deviation for the final scores is: ", np.std(final_scores))
print("\n")


#Q5-Adding 5 bonus marks for each student:
final_scores = final_scores + 5
print("Q5: The new final scores after adding a 5 mark bonus to each are: ", final_scores)
print("\n")


#Q6-Creating a Boolean array showing which students scored at least 75:
indexes=np.where(final_scores>=75)
print("Q6:")
print("A boolean array showing which students scored at least 75: ",final_scores>=75)
print("An array showing names of the students who scored at least 75: ",names[indexes])
print("\n")


#Q7- Using Boolean indexing to print only the scores greater than or equal to 75:
print("Q7: Scores greater than or equal to 75: ",final_scores[final_scores>75])
