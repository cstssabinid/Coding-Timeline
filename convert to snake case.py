def convert_to_snake(camel_string):
    snake_string = "".join(["_"+char.lower() if char .isupper() else char for char in camel_string])
    if snake_string.startswith("_"):
        snake_string = snake_string[1:]
    return snake_string
camel_case = input("Enter the variable name in camel case:")
snake_case = convert_to_snake(camel_case)
print(snake_case)
    
    