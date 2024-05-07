'''
GIVEN AN ARRAY OF INTEGERS NUMS AND AN INTEGER TARGET, RETURN INDICES OF THE TWO NUMBERS 
SUCH THAT THEY ADD UP TO TARGET.

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)
'''

def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    raise ValueError("No two sum solution")
