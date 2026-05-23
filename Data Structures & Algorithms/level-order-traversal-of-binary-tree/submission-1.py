# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #try to implement with DFS?
        stack = [[root, 0]]
        res = []

        while stack:
            node, depth = stack.pop()
            if not node:
                continue
            if len(res) == depth:
                res.append([])
                    
            res[depth].append(node.val)

            #push right first so left (last in) is processed first
            stack.append([node.right, 1 + depth])
            stack.append([node.left, 1 + depth])
        
        return res
                
            
                
        