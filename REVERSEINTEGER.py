Input: 123
Output: 321

def reverse_integer(x):
    rev = 0
    sign = 1 if x >= 0 else -1
    x = abs(x)
    while x != 0:
        pop = x % 10
        x //= 10
        rev = rev * 10 + pop
    return 0 if rev > pow(2, 31) - 1 else rev * sign
