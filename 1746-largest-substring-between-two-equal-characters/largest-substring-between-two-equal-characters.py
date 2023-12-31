class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        low = 0
        high = len(s)-1

        dp = [[-1 for i in range(len(s)+1)] for j in range(len(s)+1)]
        return self.func(low,high,dp,s)

    def func(self,low,high,dp,s):
        if(s[low] == s[high]):
            return high-low-1
        
        if(dp[low][high] !=-1):
            return dp[low][high]
        
        dp[low][high] =  max(self.func(low+1,high,dp,s),self.func(low,high-1,dp,s))
        return dp[low][high]
        



        