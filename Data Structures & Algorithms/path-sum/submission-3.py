# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return (self.path(root, targetSum, 0))


    def path(self, root, target, curVal):
        curVal+=root.val
    
        if (curVal==target and not root.left and (not root.right)):
           
            return True
         
        
        else:
            right=False
            left=False
            if root.left:
                left=self.path(root.left, target, curVal)
            if root.right:
                right=self.path(root.right, target, curVal)
        
        return (right or left or False)



        