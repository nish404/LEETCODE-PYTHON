'''
GIVEN A STRING CONTAINING JUST THE CHARACTERS '(', ')', '{', '}', '[' AND ']', 
DETERMINE IF THE INPUT STRING IS VALID

Input: "()[]{}"
Output: true
'''

def is_valid(s):
    stack = []  # Create a stack to store opening parentheses
    for c in s:  # Loop through each character in the string
        if c in '([{':  # If it's an opening parenthesis
            stack.append(c)  # Push it onto the stack
        elif not stack or (c == ')' and stack[-1] != '(') or \  # If it's a closing parenthesis and stack is empty or
                          (c == ']' and stack[-1] != '[') or \
                          (c == '}' and stack[-1] != '{'):
            return False  # Not valid
        else:
            stack.pop()  # Pop the matching opening parenthesis
    return not stack  # If stack is empty, all parentheses matched

