'''
GIVEN A STRING S, FIND THE LENGTH OF THE LONGEST SUBSTRING WITHOUT REPEATING CHARCTERS

Input: "abcabcbb"
Output: 3 ("abc" is the longest substring without repeating characters)
'''

def length_of_longest_substring(s):
    maxLength = 0  # Initialize the maximum length of substring without repeating characters
    charIndexMap = {}  # Dictionary to store the index of each character
    left = 0  # Initialize the left pointer of the window
    for right in range(len(s)):  # Iterate through the string using the right pointer
        if s[right] in charIndexMap:  # If the character is already in the dictionary
            # Move the left pointer to the next position after the last occurrence of the character
            left = max(left, charIndexMap[s[right]] + 1)
        charIndexMap[s[right]] = right  # Update the index of the character in the dictionary
        # Update the maximum length by comparing with the current window size
        maxLength = max(maxLength, right - left + 1)
    return maxLength  # Return the maximum length of substring without repeating characters
