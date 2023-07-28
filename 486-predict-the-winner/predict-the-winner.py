class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dp = {}
        n1,n2 = 0,len(nums)-1
        temp = self.dfs(nums,n1,n2,dp)
        return (temp>=sum(nums)-temp)
        

    def dfs(self,nums,n1,n2,dp):
        if(n1>n2):
            return 0
        if(n1 == n2):
            return nums[n1]

        if(n1 in dp):
            if(n2 in dp[n1]):
                return dp[n1][n2]

        ans = max(nums[n1]+min(self.dfs(nums,n1+2,n2,dp),self.dfs(nums,n1+1,n2-1,dp)),nums[n2]+min(self.dfs(nums,n1+1,n2-1,dp),self.dfs(nums,n1,n2-2,dp)))

        if(n1 not in dp):
            dp[n1] = {}
        dp[n1][n2] = ans
        return dp[n1][n2]

