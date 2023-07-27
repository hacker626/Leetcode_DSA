class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        low = 0
        high = 0
        dict_ = {0:0}
        ans = 0
        while(high<len(nums)):
            if(nums[high] == 0):
                dict_[0] += 1
            if(dict_[0]>1):
                ans = max(ans,high-low-1)
                while(dict_[0]>1):
                    if(nums[low] == 0):
                        dict_[0]-=1
                    low+=1
            high+=1
        return max(ans,high-low-1)
