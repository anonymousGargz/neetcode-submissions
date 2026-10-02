# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #Basically like a BFS
        ans=[]
        myQueue=[]
        myQueue.append(root)
        if not root:
            return []
        while myQueue:
            level=[]
            ansLevel=[]
            for node in myQueue:
                ansLevel.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            ans.append(ansLevel)
            myQueue=level
        return ans
        

