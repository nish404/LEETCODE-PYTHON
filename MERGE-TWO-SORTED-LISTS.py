'''
MERGE TWO SORTED LINKED LISTS AND RETURN IT AS A NEW SORTED LIST 

Input: l1 = 1->2->4, l2 = 1->3->4
Output: 1->1->2->3->4->4
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l1 else l2
    return dummy.next
