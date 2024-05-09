'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

class Solution(object):
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
