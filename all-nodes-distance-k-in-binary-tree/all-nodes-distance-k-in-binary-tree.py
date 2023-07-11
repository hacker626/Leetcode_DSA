# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        graph = {}
        # temp = {}
    
        self.inOrder(root,graph)
        # print(graph)
        vis = {}
        for i in graph:
            vis[i] = -1
        # for i in graph[target]:
        #     print(i)
        ans = []
        vis[target.val] = 1
        self.dfs(graph,ans,k,target.val,vis)
        
        return ans


        # return []
    def dfs(self,graph,ans,k,target,vis):
        if(k == 0):
            ans.append(target)
            return

        temp = graph[target]
        for i in temp:
            if(vis[i] == -1):
                vis[i] = 1
                self.dfs(graph,ans,k-1,i,vis)
    def inOrder(self,root,graph):
        if(root == None):
            return 
        if(root.val not in graph):
            graph[root.val] = []
        if(root.left):
            graph[root.val].append(root.left.val)
            graph[root.left.val] = [root.val]
        if(root.right):
            graph[root.val].append(root.right.val)
            graph[root.right.val] = [root.val]
        self.inOrder(root.left,graph)
        self.inOrder(root.right,graph)


            










