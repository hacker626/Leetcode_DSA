class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low,hi = 0,len(nums)-1

        while(low<=hi):
            mid = low+(hi-low)//2

            if(nums[mid] == target):
                return mid
            elif(nums[mid]>target):
                hi = mid-1
            else:
                low = mid+1
        return -1
        