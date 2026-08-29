#Defining a function to check whether a number is prime or not:

def is_prime(n):
    for i in range(2, int(n**0.5+1)):
        if n%i==0:
            return False
            break
    else:
        return True


#Taking User Input:

num = int(input("Enter the number you want to test: "))
print(is_prime(num))


#Using my function to print all prime numbers from 2 to the entered number:
prime_list=[]
for j in range(2,num+1):
    if is_prime(j)==True:
        prime_list.append(j)
print("The prime numbers upto that number are: ", prime_list)