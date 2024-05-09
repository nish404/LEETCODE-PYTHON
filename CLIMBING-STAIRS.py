'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''

class Solution:
    def longestCommonPrefix(self, strs):
        # Check if the input list is empty
        if not strs:
            return ""

        # Initialize the common prefix as the first string in the list
        common_prefix = strs[0]

        # Iterate through the remaining strings in the list
        for string in strs[1:]:
            # If the common prefix is empty, there can't be any common prefix
            if not common_prefix:
                break

            # Initialize the new common prefix as an empty string
            new_prefix = ""

            # Iterate through each character in the current common prefix and the current string
            for char1, char2 in zip(common_prefix, string):
                # If the characters match, add the character to the new common prefix
                if char1 == char2:
                    new_prefix += char1
                else:
                    # If the characters don't match, break the loop as the common prefix ends here
                    break

            # Update the common prefix with the new common prefix
            common_prefix = new_prefix

        return common_prefix
