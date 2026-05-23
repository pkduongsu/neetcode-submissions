# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = [root]
        
        if not root:
            return root
        
        while s:
            current = s.pop()
            temp = current.left
            current.left = current.right
            current.right = temp
            
            if current.left:
                s.append(current.left)
            if current.right:
                s.append(current.right)

        return root


    
        
        