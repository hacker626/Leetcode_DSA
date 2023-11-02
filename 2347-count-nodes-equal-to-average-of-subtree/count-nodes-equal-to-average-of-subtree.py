# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        count = [0]
        self.func(root,count)
        return count[0]
    
    def func(self,root,count):

        if(root == None):
            return [0,0]

        left = self.func(root.left,count)
        right = self.func(root.right,count)

        totalsum = left[0]+right[0]+root.val
        div = left[1]+right[1]+1


        if(totalsum/div == root.val):
            count[0]+=1
        return [totalsum,div]
        