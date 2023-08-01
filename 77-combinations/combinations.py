class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """


        ans = []
        return self.func(n,k,ans,[],0)
        # return ans


    def func(self,n,k,ans,temp,start):
        if(len(temp) == k):
            ans.append(temp)
            return ans


        for i in range(start+1,n+1):
            temp1 = temp+[i]
            self.func(n,k,ans,temp1,i)
        return ans
        