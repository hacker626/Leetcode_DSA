import math
class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        if(n>4800):
            return 1.0


        n = math.ceil(n/25.0)
        dp = {}
        return self.recMem(n,dp,n,n)

    def recMem(self,n,dp,i,j):

        if(i<=0 and j<=0):
            return 0.5
        elif(i<=0):
            return 1.0
        elif(j<=0):
            return 0.0
        if((i,j) in dp):
            return dp[(i,j)]
        dp[(i,j)] = 0.25*(self.recMem(n,dp,i-4,j)+self.recMem(n,dp,i-3,j-1)+self.recMem(n,dp,i-2,j-2)+self.recMem(n,dp,i-1,j-3))
        return dp[(i,j)]

        