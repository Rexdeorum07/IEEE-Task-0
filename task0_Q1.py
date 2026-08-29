#Declaring the necessary variables

count= int(input("Enter the count of your numbers: "))
num_list=[]
num_added=0
temp_list=[]


#taking input form the user utilizing a loop

for i in range(1, (count+1)):
    num_added = int(input(f"Enter number {i}: "))
    num_list.append(num_added)


#the sorting algorithm

temp_list.insert(0, num_list[0])

for i in range(1,len(num_list)):
    if num_list[i]>=temp_list[len(temp_list)-1]:
        temp_list.append(num_list[i])

    else:
        current_index=len(temp_list)-1
        while(num_list[i]<temp_list[current_index]):
            current_index -= 1
            if current_index<0 or num_list[i]>temp_list[current_index]:
                temp_list.insert(current_index+1, num_list[i])
                break
            if num_list[i]==temp_list[current_index]:
                temp_list.insert(current_index, num_list[i])
                break


#Summation algorithm

summation=0
k=0
while k<=(len(num_list)-1):
    summation=summation + num_list[k]
    k+=1

#Counting of Even Numbers algorithm

even_count=0
for l in range(len(num_list)):
    if num_list[l] % 2 == 0:
        even_count+=1


#Printing the answers
print("*******************************************************")
print("1. Your entered list of numbers is: ",num_list)
print("2. The largest element is:", temp_list[len(temp_list)-1])
print("3. The smallest element is:", temp_list[0])
print("4. The sum of all elements is:", summation)
print("5. The number of even elements is:", even_count)
print("The number of odd elements is:", len(num_list)-even_count)
num_list.reverse()
print("6. The reverse order of your entered list is:", num_list)