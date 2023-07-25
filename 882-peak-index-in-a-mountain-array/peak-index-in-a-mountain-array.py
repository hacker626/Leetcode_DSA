class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        low,high = 0,n-1

        while(low<=high):
            mid=low+(high-low)//2

            if(arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
                return mid
            elif(mid>0 and arr[mid]<arr[mid-1]):
                high=mid-1
            else:
                low=mid+1
        # return high
            