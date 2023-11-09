max_num = None
min_num = None
while True:
    input_num =input("Enter the number of done:")
    if input_num.lower() == 'done':
        break
    try:
        num = int(input_num)
    except ValueError:
        print("Invalid input, Just enter a valid integer or 'done'")
        continue    
    if max_num is None or num > max_num:
        max_num = num
    if min_num is None or num < min_num:
        min_num = num
if max_num is not None and min_num is not None:
        print("Largest is:",max_num)
        print("smallest is:",min_num)
else :
        print("No valid integer entered!")    