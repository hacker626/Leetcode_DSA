class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low,hi=0,n-1
        if(n == 1):
            return 0
        if(n >= 2):
            if(nums[0]>nums[1]):
                return 0
            elif(nums[-1]>nums[-2]):
                return n-1


        while(low<=hi):
            mid = low+(hi-low)//2

            if(0<mid<n-1 and nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
                return mid
            elif(mid>0 and nums[mid]<nums[mid-1]):
                hi=mid-1
            else:
                low=mid+1

        