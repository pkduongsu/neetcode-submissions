# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        n = 0 #number of visited elements
        current = root

        while stack or current:
            while current:
                stack.append(current) #add the visited node
                current = current.left #and move the pointer to  the left node (with smaller values)

            #after all smaller values are added (current becomes null)
            current = stack.pop()
            n += 1
            if n == k:
                return current.val   
            current = current.right



        