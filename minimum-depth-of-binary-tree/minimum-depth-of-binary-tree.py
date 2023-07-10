# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.inOrder(root,float('inf'))


    def inOrder(self,root,ans):
        if(root == None):
            return 0
        if(root.left == None):
            ans = min(ans,1+self.inOrder(root.right,ans))
        elif(root.right == None):
            ans = min(ans,1+self.inOrder(root.left,ans))
        elif(root.left == None and root.right == None):
            return 1
        else:
            ans = min(ans,1+self.inOrder(root.right,ans),1+self.inOrder(root.left,ans))


        return ans