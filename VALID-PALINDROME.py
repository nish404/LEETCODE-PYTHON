'''
DETERMINE IF THE STRING IS A VALID PALINDROME
'''

def is_palindrome(string):
    # Base case: if the string is empty, it is considered a palindrome
    if len(string) == 0:
        return True
    
    # Initialize variables for the start and end of the string
    start = 0  # Start at the beginning of the string
    end = len(string) - 1  # Start at the end of the string
    
    # Iterate until the start index is less than the end index
    while start < end:
        if string[start] == string[end]:  # If characters at start and end are the same
            start += 1  # Move start index forward
            end -= 1  # Move end index backward
        else:  # If characters are not the same, the string is not a palindrome
            print(f'"{string}" is not a palindrome')
            return False
    
    # If the loop completes without returning false, the string is a palindrome
    print(f'"{string}" is a palindrome')
    return True

# Test the function with some examples
is_palindrome("racecar")  # Output: "racecar" is a palindrome
is_palindrome("hello")  # Output: "hello" is not a palindrome
is_palindrome("")  # Output: "" is a palindrome since it's empty
