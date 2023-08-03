# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        ans = [0]
        self.func(root,ans)
        return ans[0]
    def func(self,root,ans):
        if(root == None):
            return 0


        l = self.func(root.left,ans)
        r = self.func(root.right,ans)

        ans[0] = max(ans[0],l+r)

        return 1+max(l,r)
        