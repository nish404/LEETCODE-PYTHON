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

