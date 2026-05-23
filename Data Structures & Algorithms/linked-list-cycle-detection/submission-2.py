# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        #why?
        #fast, slow = 1, 1
        #while fast and fast next:
        # slow = 2
        #fast = 3
        #slow != fast -> next
        #slow = 3, fast = 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False