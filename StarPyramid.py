def star_pyramid(p_len):
    for i in range(p_len):
        space = " " *(p_len - i - 1)
        starz = "*" *(2 * i - 1)
        print (space+starz)
try:
    length = int(input("Enter the lenght of the pyramidy you desire:"))
    len = star_pyramid(length)
except ValueError:
    print("Please enter the valid integer")