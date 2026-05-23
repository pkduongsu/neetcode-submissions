# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       #first question to ask is: is there any upper/lower boundaries for a node's value?
       # if they answer, ex: not infinite, but [-1000, 1000]:
       # go ahead and explain the boundary approach
       # Root node: Boundary: [-1000, 1000], Value: node.val
       # Left node: Boundary: [-1000, node.val], Value: node.left -> needs to check it against the boundaries, false -> return false (not valid BST)
       # Same for the right node: [node.val, 1000], Value: node.right -> if false, return false
       # With this logic, we now only need to implement it with a traversal algo: BFS, DFS, Iterative DFS

       #BFS: Queue (LIFO)
       #Iterative DFS: Stack (FIFO)
        q = deque([[root, -1000, 1000]])
    
        def isValidNode(node: TreeNode, left, right) -> bool:
            if (node.val > left and node.val < right):
                return True
            else: return False

        if not root:
            return True
        
        while q:
            current, left, right = q.popleft()

            if not isValidNode(current, left, right):
                return False
            
            if current.left:
                q.append([current.left, left, current.val])

            if current.right:
                q.append([current.right, current.val, right])

        return True
            



        

        