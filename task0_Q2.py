numbers=[]
count= int(input("Enter the count of your numbers: "))

for i in range(1, (count+1)):
    num_added = int(input(f"Enter number {i}: "))
    numbers.append(num_added)

def process_list(numbers):
    i=0
    numbers_copy = numbers.copy()
    k=len(numbers_copy)

    while i<=k-1:
        if numbers_copy[i]<0:
            numbers_copy.pop(i)
            i=0
            k-=1
        else:
            i+=1


    numbers_copy.append(0)
    numbers_copy.sort()
    return numbers_copy

result= process_list(numbers)
print("Original:",numbers)
print("Result:",result)


