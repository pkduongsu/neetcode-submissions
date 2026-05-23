# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #remove: detach the link of that list
        #-> next pointer of the previous node points to the next of next node
        #self.next = current.next.next 
        #input: head node, n: index of the node to remove
        # output: the new head node 
        #problem is, how would we know the index of the listNode?
        # needs to keep track with something, like a hashmap?
        #ask how the index is tracked (zero indexed or 1-indexed)
        #1-indexed, and the node is the nth node FROM THE END OF THE LIST

        #question is, how can we go back to the previous node?
        #question 2: we don't even know the length of the linked list initially

        current = head
        nodesList = []

        while current:
            nodesList.append(current)
            current = current.next

        removeIndex = len(nodesList) - n
        if (removeIndex == 0):
            return head.next

        nodesList[removeIndex - 1].next = nodesList[removeIndex].next

        return head
        