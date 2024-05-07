'''
MERGE TWO SORTED LINKED LISTS AND RETURN IT AS A NEW SORTED LIST 

Input: l1 = 1->2->4, l2 = 1->3->4
Output: 1->1->2->3->4->4
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Initialize the value of the node
        self.next = next  # Initialize the next node reference

def merge_two_lists(l1, l2):
    dummy = ListNode()  # Create a dummy node for the merged list
    current = dummy  # Initialize current pointer to the dummy node
    while l1 and l2:  # Continue until either list becomes empty
        if l1.val < l2.val:  # If value in l1 is smaller
            current.next = l1  # Append l1 to the merged list
            l1 = l1.next  # Move to the next node in l1
        else:  # If value in l2 is smaller or equal
            current.next = l2  # Append l2 to the merged list
            l2 = l2.next  # Move to the next node in l2
        current = current.next  # Move current pointer to the newly added node
    current.next = l1 if l1 else l2  # Append the remaining nodes from the non-empty list
    return dummy.next  # Return the merged list starting from the next node of the dummy
