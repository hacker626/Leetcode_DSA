class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        i,j = 0,0
        ans = float('inf')
        currSum = 0
        while(j<len(nums)):
            currSum+=nums[j]
            if(currSum>=target):
                while(currSum>=target):
                    ans = min(ans,j-i+1)
                    currSum-=nums[i]
                    i+=1
            
            j+=1
        return ans if(ans!=float('inf')) else 0

                    