# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #input: head: Optional[ListNode]

        res = {}
        current = head

        while current: 
            res[current] = res.get(current, True)
            if (current.next in res):
                return True
            current = current.next

        return False

