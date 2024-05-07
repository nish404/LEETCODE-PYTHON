'''
GIVEN A STRING CONTAINING JUST THE CHARACTERS '(', ')', '{', '}', '[' AND ']', 
DETERMINE IF THE INPUT STRING IS VALID

Input: "()[]{}"
Output: true
'''

def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
