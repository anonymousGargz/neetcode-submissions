# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans=[]
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.parse(root,0)
        return self.ans

    
    def parse(self, root, level):
        if root is None:
            return
        
        if len(self.ans)==level:
            self.ans.append([])
        
        self.ans[level].append(root.val)
        
        self.parse(root.left, level+1)
        self.parse(root.right, level+1)
    


        