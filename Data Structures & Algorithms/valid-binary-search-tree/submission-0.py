# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #left boundary and right boundary: condition for the current node
        def isValidNode(node: TreeNode, left, right) -> bool:
            if not node: #for any recursive, hit null -> return 
                return True

            if not (node.val < right and node.val > left):
                return False

            return (isValidNode(node.left, left, node.val) 
            and isValidNode(node.right, node.val, right))

        return isValidNode(root, float("-inf"), float("inf"))

        

        