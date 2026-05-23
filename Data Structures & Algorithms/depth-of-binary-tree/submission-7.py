# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #given root, return maximum depth
        #we think of traversing through the tree and memorize the current depth of node somehow
        #-> stack element will be the node, along with its depth (init by root, 1)
        #if we append the node on lower depth (left, right), append with the prev node depth + 1
        #update a global value for memorizing max depth
        q = deque([[root, 1]])

        if not root:
            return 0

        maxDepth = 0
        while q:
            currentNode, currentDepth = q.popleft()

            maxDepth = max(maxDepth, currentDepth)

            if currentNode.left:
                q.append([currentNode.left, currentDepth + 1])
            if currentNode.right:
                q.append([currentNode.right, currentDepth + 1])

        return maxDepth
        



        
        