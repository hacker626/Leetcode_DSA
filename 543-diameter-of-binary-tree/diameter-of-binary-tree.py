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
        temp = [0]
        self.func(root,temp)
        return temp[0]


    def func(self,root,temp):
        if(root == None):
            return 0

        lv = self.func(root.left,temp)
        rv = self.func(root.right,temp)
        temp[0] = max(temp[0],lv+rv)

        return 1+max(lv,rv)
        