# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        return self.inOrder(root,low,high)



    def inOrder(self,root,low,high):
        if(root == None):
            return 0
            

        
        if(low<=root.val<=high):
            return self.inOrder(root.left,low,high)+root.val+self.inOrder(root.right,low,high)
        else:
            return self.inOrder(root.left,low,high)+self.inOrder(root.right,low,high)
        
        