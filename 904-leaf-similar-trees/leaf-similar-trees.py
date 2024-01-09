# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        ans1,ans2 = [],[]
        self.func(root1,ans1)
        self.func(root2,ans2)
        return ans1 == ans2


    def func(self,root,ans):
        if(root == None):
            # ans.append(root.val)
            return 
        self.func(root.left,ans)
        if(root.left == None and root.right == None):
            ans.append(root.val)
        self.func(root.right,ans)

        