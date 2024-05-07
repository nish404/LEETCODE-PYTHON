'''
GIVEN A STRING S, FIND THE LENGTH OF THE LONGEST SUBSTRING WITHOUT REPEATING CHARCTERS

Input: "abcabcbb"
Output: 3 ("abc" is the longest substring without repeating characters)
'''

def length_of_longest_substring(s):
    maxLength = 0
    charIndexMap = {}
    left = 0
    for right in range(len(s)):
        if s[right] in charIndexMap:
            left = max(left, charIndexMap[s[right]] + 1)
        charIndexMap[s[right]] = right
        maxLength = max(maxLength, right - left + 1)
    return maxLength
