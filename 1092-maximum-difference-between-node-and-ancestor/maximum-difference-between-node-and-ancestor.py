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
        ans1 = [float('-inf')]
        ans2 = [float('-inf')]
        self.func1(root,ans1)
        self.func2(root,ans2)

        return max(ans1[0],ans2[0])

    def func1(self,root,ans):
        if(root == None):
            return float('inf')

        temp = min(root.val,self.func1(root.left,ans),self.func1(root.right,ans))
        ans[0] = max(ans[0],abs(root.val-temp))
        return temp

    def func2(self,root,ans):
        if(root == None):
            return float('-inf')

        temp = max(root.val,self.func2(root.left,ans),self.func2(root.right,ans))
        ans[0] = max(ans[0],abs(root.val-temp))
        return temp
        


        
        
        # self.func(root.left,ans,small,large)


        # temp = min(self.func())
        # if(root.val<small):
        #     small = root.val
        # if(root.val>large):
        #     large = root.val
        # ans[0] = max(ans[0],abs(root.val-large),abs(root.val-small))
        # print(ans)
        # self.func(root.right,ans,small,large)


        