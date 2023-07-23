class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 1):
            return 0
        if(len(nums)>=2):
            if(nums[0]>nums[1]):
                return 0
            elif(nums[-1]>nums[-2]):
                return len(nums)-1
        n = len(nums)
        low = 0
        high = n-1
        ans = 0
        ansValue = float('-inf')
        while(low<=high):
            mid = low+(high-low)//2

            if(0<mid<n-1 and nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
                return mid
            elif(mid>0 and nums[mid]<nums[mid-1]):
                high=mid-1
            else:
                low=mid+1
        # return 8
        



