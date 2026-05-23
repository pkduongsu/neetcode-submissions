# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s1 = [p]
        s2 = [q]

        
        while s1 and s2:
            current_p = s1.pop()
            current_q = s2.pop()

            if current_p is None and current_q is None:
                continue

            if current_p is None or current_q is None or current_p.val != current_q.val:
                return False

            s1.append(current_p.left)
            s2.append(current_q.left)

            s1.append(current_p.right)
            s2.append(current_q.right)

        return True
        