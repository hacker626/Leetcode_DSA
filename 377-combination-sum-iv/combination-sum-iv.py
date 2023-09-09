class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [-1 for i in range(target+1)]
        return self.func(nums,target,dp)
    def func(self,nums,target,dp):
        if(target == 0):
            return 1
        elif(target<0):
            return 0
        if(dp[target] != -1):
            return dp[target]
        dp[target] = 0
        for i in range(len(nums)):
            dp[target] += self.func(nums,target-nums[i-1],dp)
            
        return dp[target]
        