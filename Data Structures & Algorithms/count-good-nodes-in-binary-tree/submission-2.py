# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#how do we define a tree node?
#Given that we're examining a BST:
# node: value, left, right pointers

#class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#       self.val = val
#       self.left = left
#       self.right = right

#Input: root node of a BST
#output: the number of good nodes within the tree -> int
#def GoodNodes(self, root: TreeNode) -> int:

#good node: the path from root of the tree to node x contains no nodes with a value greater than 
#value of node x

#does this include tha value of the root node?

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)

            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)

        