# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """


        graph = {}
        self.inOrder(root,graph)
        print(graph)

        # graph = {}


        vis = {}
        for i in graph:
            vis[i] = -1
        print(vis)
        count = 0
        queue = [start]
        vis[start] = 1
        while(len(queue)>0):
            count+=1
            for i in range(len(queue)):
                temp = queue.pop(0)
                for j in graph[temp]:
                    if(vis[j] == -1):
                        queue.append(j)
                        vis[j] = 1
        return count-1

        






    def inOrder(self,root,graph):
        if(root == None):
            return 
        self.inOrder(root.left,graph)
        if(root.val not in graph):
            graph[root.val] = []
        if(root.left):
            graph[root.val].append(root.left.val)
            if(root.left.val not in graph):
                graph[root.left.val] = []
            graph[root.left.val].append(root.val)
        if(root.right):

            graph[root.val].append(root.right.val)
            if(root.right.val not in graph):
                graph[root.right.val] = []

            graph[root.right.val].append(root.val)
        # graph[root.val].append(root.left)
        # node.append(root.val)
        self.inOrder(root.right,graph)

    


        
        