# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        bfs=deque()
        bfs.append(root)
        ans=[]
        if not root:
            return []
        while bfs:
            lent=len(bfs)
            temp=[]
            for i in range(0, lent):
                roo=bfs.popleft()
                temp.append(roo.val)

                if roo.left:
                    bfs.append(roo.left)
                if roo.right:
                    bfs.append(roo.right)
            ans.append(temp)
        return ans
        

                

