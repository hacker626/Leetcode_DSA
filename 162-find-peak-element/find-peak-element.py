class Solution(object):
    def findPeakElement(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(arr)
        low,high = 0,n-1
        if(n == 1):
            return 0
        if(n >= 2):
            if(arr[0]>arr[1]):
                return 0
            elif(arr[-1]>arr[-2]):
                return n-1

        while(low<=high):
            mid = low+(high-low)//2

            if(0<mid<n-1 and arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
                return mid
            elif(mid>0 and arr[mid]<arr[mid-1]):
                high = mid-1
            else:
                low = mid+1
        

        