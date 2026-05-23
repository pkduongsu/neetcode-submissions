# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#input: root node of a binary tree: root: Optional[treeNode]

#output: list of values of nodes that are visible from the right side of the tree, ordered by top to bottom
#- > list[int]

#Optional: can be none
#def RightSideView(self, root: Optional[TreeNode]) -> List[int]

#I'd say, track if it has right nodes? if not, add to the result array

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = [(root, 0)]  # (node, depth)

        while stack:
            node, depth = stack.pop()
            if node is None:
                continue

            # first time we reach this depth (since we go right-first)
            if depth == len(res):
                res.append(node.val)

            # push left first, then right so right is processed first (LIFO)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))

        return res





        
        