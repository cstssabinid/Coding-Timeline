def step_counter(num):
    count= 0
    while num != 1:
        if num % 2 == 0:
            num //=2
        else:
            num =num*3+1
        count +=1
    return count
data = int(input("Enter the number to devide:"))
use_data = step_counter(data)
print ("Steps taken to devide enter number are:",use_data)