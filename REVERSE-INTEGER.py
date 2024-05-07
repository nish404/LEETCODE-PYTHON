'''
REVERSE DIGITS OF AN INTEGER

Input: 123
Output: 321
'''

def reverse_integer(x):
    rev = 0  # Initialize the reversed number
    sign = 1 if x >= 0 else -1  # Determine the sign of the input number
    x = abs(x)  # Get the absolute value of x
    while x != 0:  # Continue until x becomes 0
        pop = x % 10  # Extract the last digit of x
        x //= 10  # Remove the last digit from x
        rev = rev * 10 + pop  # Build the reversed number
    # Check if the reversed number exceeds the 32-bit signed integer range
    return 0 if rev > pow(2, 31) - 1 else rev * sign  # Return the reversed number with sign

