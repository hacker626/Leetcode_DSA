class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        low,high = 0,len(arr)-1

        while(low<=high):
            mid = low+(high-low)//2

            if(0<mid<len(arr)-1 and arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
                return mid
            elif(mid<len(arr)-1 and arr[mid]>arr[mid+1]):
                high=mid-1
            else:
                low=mid+1
        return 0
        