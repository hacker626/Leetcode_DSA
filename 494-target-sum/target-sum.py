class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


        dp = {}
        return self.func(nums,target,len(nums),dp)


    def func(self,nums,target,n,dp):

        if(n == 0):
            if(target == 0):
                return 1
            else:
                return 0
        if( n in dp):
            if(target in dp[n]):
                return dp[n][target]
        if(n not in dp):
            dp[n] = {}

        dp[n][target] = (self.func(nums,target-nums[n-1],n-1,dp)+self.func(nums,target+nums[n-1],n-1,dp))%(10**9+7)
        return dp[n][target]
        