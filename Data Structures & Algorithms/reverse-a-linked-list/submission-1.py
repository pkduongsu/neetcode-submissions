# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #reverse using:
        #Iterative / Recursion
        #Iterative: use 2 pointer: current and previous.
        ## Previous will store the value of the previous node, so to reverse the direction of the node, 
        #set current.next = previous
        #and move on to the next node by setting the current = current.next 
        #and move the prev pointer to the current node 
        #and because of this, needs to store the initial current.next value for this before changing to prev
        

        #because there are nothing previous the first node, set prev to None
        current, prev = head, None
        
        #iterate till the node move on to None -> prev is the last node in the linked list
        #we need to return the new beginning of the list -> return prev pointer
        while current:
            temp = current.next
            current.next = prev #reverse the next pointer of the current node
            #move on to the next node:
            prev = current
            current = temp

        return prev
