'''
DETERMINE WHETHER AN INTEGER IS A PALINDROME. AN INTEGER IS A PALINDROME WHEN IT READS THE 
SAME BACKWARDS AS FORWARD.

Input: 121
Output: true
'''

def is_palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10
