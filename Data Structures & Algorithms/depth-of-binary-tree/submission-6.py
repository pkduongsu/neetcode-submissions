# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #given root, return maximum depth
        s = [[root, 1]]

        if not root:
            return 0

        maxDepth = 0
        while s:
            currentNode, currentDepth = s.pop()

            maxDepth = max(maxDepth, currentDepth)

            if currentNode.left:
                s.append([currentNode.left, currentDepth + 1])
            if currentNode.right:
                s.append([currentNode.right, currentDepth + 1])

        return maxDepth
        



        
        