'''
GIVEN AN ARRAY OF NUMS OF SIZE N, RETURN THE MAJORITY ELEMENT (APPEARS MORE
THAN N/2 TIMES). YOU MAY ASSUME THAT THE MAJORITY ELEMENT ALWAYS EXISTS IN 
THE ARRAY.

Input: [3,2,3]
Output: 3
'''

def majority_element(nums):
    candidate = None  # Initialize the candidate element
    count = 0  # Initialize the count of occurrences

    # Iterate through the list of numbers
    for num in nums:
        if count == 0:
            # If the count is 0, update the candidate to the current number
            candidate = num
        # Increment or decrement the count based on whether the number matches the candidate
        count += 1 if num == candidate else -1

    return candidate  # Return the majority element
