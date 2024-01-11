# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def func(root,low,high,ans):
            if(root == None):
                return
            ans[0] = max(ans[0],abs(root.val-low),abs(root.val-high))
            func(root.left,min(low,root.val),max(high,root.val),ans)
            func(root.right,min(low,root.val),max(high,root.val),ans)
        ans = [0]
        func(root,root.val,root.val,ans)
        return ans[0]


        