# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])

        if not root:
            return None

        while q:
            current = q.popleft()
            current.left, current.right = current.right, current.left

            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

        return root
    
        
        