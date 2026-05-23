# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# self.val, self.left, self.right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []

        # #can somehow mark the level of the node?
        # #now that we have the level of the node, how can we print out the output in the format 
        # #where each level is a subarray that has all the nodes of that level?

        # #order of the node? 
        # #declared in the problem statement: 

        # s = [[root, 0]]
        # res = []

        # while s:
        #     current, depth = s.pop()

        #     if len(res) == depth:
        #         res.append([])

        #     res[depth].append(current.val) #depth as the index for sublists in the result array to add respective nodes

        #     if current.right:
        #         s.append([current.right, depth + 1])
        #     if current.left:
        #         s.append([current.left, depth + 1])

        # return res
                

        #BFS: use a queue to solve the problem
        
        if not root:
            return []

        q = deque([[root, 0]])
        res = []

        while q:
            current, depth = q.popleft()

            if len(res) == depth:
                res.append([])

            res[depth].append(current.val)

            if current.left:
                q.append([current.left, depth + 1])
            if current.right:
                q.append([current.right, depth + 1])

        return res

            


        