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
    def inOrder(self,root,store):

        if(root == None):
            return
        store[1]+=1
        self.inOrder(root.left,store)
        store[0]+=root.val
        # store[1]+=1

        self.inOrder(root.right,store)
    def func(self,root,count):

        if(root == None):
            return 
        self.func(root.left,count)
        store = [0,0]
        self.inOrder(root,store)
        # print(store,store[0]/store[1],root.val)
        if(store[0]/store[1] == root.val):
            count[0]+=1
        self.func(root.right,count)
        # return count
        
        


        