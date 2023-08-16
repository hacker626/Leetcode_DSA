class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        low,high = 0,0
        maxNum = []
        ans = []
        while(high<len(nums)):
            while(len(maxNum)>0 and maxNum[-1]<nums[high]):
                maxNum.pop()
            maxNum.append(nums[high])
            if(high-low+1 == k):
                ans.append(maxNum[0])
                if(maxNum[0] == nums[low]):
                    maxNum.pop(0)
                low+=1
            high+=1
        return ans

        