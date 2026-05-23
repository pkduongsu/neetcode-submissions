# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Input: beginning of a singly linkedin list  - head
        #Output: the new begininng of the list, which other nodes points to the reverse of original linked list
        #Ex: 1 -> 2 -> 3 -> 4 => 4 -> 3 -> 2 -> 1

        prev, current = None, head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev



