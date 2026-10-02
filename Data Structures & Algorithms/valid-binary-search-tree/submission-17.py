# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return (self.search(root, float("-inf"), float("inf")))
    

    def search(self, root, left, right):
        if not root:
            return True
        else:
            ans=False
            if (root.val> left and root.val<right):
                ans=True
            else:
                return False
            newLeft=self.search(root.left, left, root.val)
            newRight= self.search(root.right, root.val, right)
        
        return (ans and newLeft and newRight)
    


