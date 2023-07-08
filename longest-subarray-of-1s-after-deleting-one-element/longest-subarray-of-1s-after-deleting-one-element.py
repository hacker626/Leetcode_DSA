class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        low,high = 0,0
        index0 = -1
        ans = float('-inf')
        while(high<len(nums) and low<len(nums)):
            if(nums[high] == 0):
                if(index0 == -1):
                    index0 = high
                else:
                    ans = max(ans,high-low-1)
                    while(index0 != low):
                        low+=1
                    low+=1
                    index0 = high
            high+=1
        return max(ans,high-low-1)
                    