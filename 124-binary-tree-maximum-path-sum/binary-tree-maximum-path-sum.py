# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [float('-inf')]
        self.func(root,ans)
        return ans[0]

    def func(self,root,ans):

        if(root == None):
            return 0
        l = max(0,self.func(root.left,ans))
        r = max(0,self.func(root.right,ans))

        ans[0] = max(ans[0],root.val+l+r)


        return root.val+max(l,r)
        