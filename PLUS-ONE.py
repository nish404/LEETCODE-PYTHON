'''
You are given a large integer represented as an integer array digits, where each digits[i]
is the ith digit of the integer. The digits are ordered from most significant to least 
significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1
Input: digits = [1,2,3]
Output: [1,2,4]
Explaination: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explaination: The array represents the integer 4321. Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3
Input: [9]
Output: [1,0]
Explaination: The array represents an integer of 9. Increment by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's
'''

def plus_one(digits):
    # Start from the rightmost digit
    n = len(digits)
    # Iterate through the digits in reverse order
    for i in range(n - 1, -1, -1):
        # Increment the current digit by 1
        digits[i] += 1
        # If the digit is less than 10, no carry is needed, so return the digits
        if digits[i] < 10:
            return digits
        else:
            # Carry occurs, set the current digit to 0 and continue to the next digit
            digits[i] = 0
    
    # If the loop completes and there's still a carry, insert 1 at the beginning
    return [1] + digits

# Test the function with some examples
print(plus_one([1, 2, 3]))  # Output: [1, 2, 4]
print(plus_one([9, 9, 9]))  # Output: [1, 0, 0, 0]
