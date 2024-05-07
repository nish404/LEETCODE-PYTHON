'''
GIVEN AN ARRAY OF INTEGERS NUMS AND AN INTEGER TARGET, RETURN INDICES OF THE TWO NUMBERS 
SUCH THAT THEY ADD UP TO TARGET.

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)
'''

def two_sum(nums, target):
    hashmap = {}  # Initialize a dictionary to store the complement and its index
    for i, num in enumerate(nums):  # Iterate through the list with index
        complement = target - num  # Calculate the complement for the current number
        if complement in hashmap:  # If complement is in the dictionary
            return [hashmap[complement], i]  # Return indices of the two numbers
        hashmap[num] = i  # Add the current number and its index to the dictionary
    raise ValueError("No two sum solution")  # Raise an error if no solution is found

