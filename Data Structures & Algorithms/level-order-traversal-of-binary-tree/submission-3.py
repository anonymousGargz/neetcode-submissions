# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        myList=[]
        myQueue=deque()
        myQueue.append(root)
        if root is None:
            return []
        while (myQueue):
            subList=[]
            for i in range(0, len(myQueue)):
                curNode=myQueue.popleft()
                subList.append(curNode.val)
                if curNode.left:
                    myQueue.append(curNode.left)
                if curNode.right:
                    myQueue.append(curNode.right)
            myList.append(subList)
        return myList
        