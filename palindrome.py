def is_palindrome(s):
    if len(s) <= 1:
        return True

    if s[0].lower() == s[-1].lower():
        return is_palindrome(s[1:-1])
    else:
        return False
    
string = input("Enter the string:")
rstring = is_palindrome(string)
print(rstring)