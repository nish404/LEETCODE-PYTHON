'''
DETERMINE WHETHER AN INTEGER IS A PALINDROME. AN INTEGER IS A PALINDROME WHEN IT READS THE 
SAME BACKWARDS AS FORWARD.

Input: 121
Output: true
'''

def is_palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0): return False  # Negative numbers and multiples of 10 (excluding 0) are not palindromes
    reversed_num = 0  # Initialize variable to store reversed number
    while x > reversed_num:  # Reverse half of the number
        reversed_num = reversed_num * 10 + x % 10  # Add last digit of x to reversed_num
        x //= 10  # Remove last digit from x
    return x == reversed_num or x == reversed_num // 10  # Check if x is equal to reversed_num or half of reversed_num (for odd digit length)

def is_palindrome(number):
    # Convert the number to a string for easier manipulation
    num_str = str(number)
    
    # Calculate the length of the string
    length = len(num_str)
    
    # Initialize two pointers, one at the beginning and one at the end of the string
    start = 0
    end = length - 1
    
    # Loop until the pointers meet or cross each other
    while start < end:
        # Compare the characters at the current pointers
        if num_str[start] != num_str[end]:
            # If they are not equal, the number is not a palindrome
            return False
        
        # Move the pointers towards each other
        start += 1
        end -= 1
    
    # If the loop completes without returning False, the number is a palindrome
    return True

# Test the function with some examples
print(is_palindrome(121))  # True
print(is_palindrome(12321))  # True
print(is_palindrome(1221))  # True
print(is_palindrome(12345))  # False
