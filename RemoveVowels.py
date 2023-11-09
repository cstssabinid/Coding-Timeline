def remove_vowels(input_string):
    vowels = "aiueoAIUEO"
    result_string = ""
    for char in input_string:
        if not char in vowels:
            result_string += char
    return result_string
input_str = input("Enter the Sample String:")
result_str = remove_vowels(input_str)
print("String without vowels:", result_str)    