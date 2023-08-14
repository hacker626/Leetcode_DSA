class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]

        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if(text1[i-1] == text2[j-1]):
                    dp[j][i] = 1+dp[j-1][i-1]
                else:
                    dp[j][i] = max(dp[j-1][i],dp[j][i-1])
        # return self.func(text1,text2,len(text1),len(text2),dp)
        return dp[-1][-1]


    # def func(self,t1,t2,n1,n2,dp):
    #     if(n1 == 0 or n2 == 0):
    #         return 0

    #     if(dp[n2][n1] != -1):
    #         return dp[n2][n1]

    #     if(t1[n1-1] == t2[n2-1]):
    #         dp[n2][n1] =  1+self.func(t1,t2,n1-1,n2-1,dp)
    #     else:
    #         dp[n2][n1] =  max(self.func(t1,t2,n1-1,n2,dp),self.func(t1,t2,n1,n2-1,dp))
    #     return dp[n2][n1]
        