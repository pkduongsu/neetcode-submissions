# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #input: head: Optional[ListNode]
        #time: O(n) where n is the length of the linked list
        #space: O(n)

        res = {}
        current = head

        while current: 
            if (current.next in res):
                return True

            res[current] = res.get(current, True)
            current = current.next

        return False

