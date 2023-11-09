import re

def sum_integers_in_file(file_name):

    with open(file_name, 'r') as file:
        data = file.read()
            
        integers = re.findall('[0-9]+', data)
        
        total_sum = sum(int(x) for x in integers)            
        return total_sum

file_name = input("Enter the name of the file: ")
total_sum = sum_integers_in_file(file_name)

print("Sum of integers in",file_name,":",total_sum)
