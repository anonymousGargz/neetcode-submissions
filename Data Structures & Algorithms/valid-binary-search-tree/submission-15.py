# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        searchRes=self.search(root, 1000000000, -10000000)
        return (searchRes)
    


    def search(self, root, maxi, mini):
        if (root.val<= mini or root.val>= maxi):
            return False
        else:
            left=True
            right=True
            if root.left:
                left=self.search(root.left, root.val, mini)
            if root.right:
                right=self.search(root.right, maxi, root.val)
        
        return (True and left and right)


        