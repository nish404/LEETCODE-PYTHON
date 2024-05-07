'''
CONVERT A ROMAN NUMERAL TO AN INTEGER

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
	• I can be placed before V (5) and X (10) to make 4 and 9. 
	• X can be placed before L (50) and C (100) to make 40 and 90. 
	• C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
 
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

'''

def roman_to_int(s):
    # Create a dictionary to map Roman numerals to integers
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Initialize the result variable
    number = 0

    # Iterate through the input Roman numeral string
    for i in range(len(s)):
        # If we are at the last character, simply add its value to the result
        if i == len(s) - 1:
            number += roman_values[s[i]]
        else:
            # Otherwise, compare the current value with the next value
            current_value = roman_values[s[i]]
            next_value = roman_values[s[i + 1]]

            if current_value < next_value:
                # If current value is less than the next value, subtract it
                number -= current_value
            else:
                # Otherwise, add it to the result
                number += current_value

    return number  # Return the resulting integer
