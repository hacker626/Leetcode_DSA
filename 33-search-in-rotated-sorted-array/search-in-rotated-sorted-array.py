class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        arr=nums[:]
        # if(nums[0] == target):
        #     return 0
        # elif(nums[-1] == target):
        #     return n-1
        # if(n<=3):
        #     for i in range(n):
        #         if(arr[i] == target):
        #             return i
        #     return -1
        def bSearch(arr,s,e,target):


            while(s<=e):
                mid = s+(e-s)//2
                if(arr[mid] == target):
                    return mid
                elif(arr[mid]>target):
                    e=mid-1
                else:
                    s=mid+1
            return -1
        def rotate(nums):

            if(nums[0]<nums[-1]):
                return 0
            low,high = 0,len(nums)-1
            # k = -1
            while(low<=high):
                mid = low+(high-low)//2
                if(0<mid<n-1 and arr[mid]<arr[mid-1] and arr[mid]<arr[mid+1]):
                    return mid
                elif(arr[mid]<arr[-1]):
                    high=mid-1
                else:
                    low=mid+1
            return len(nums)-1
        k = rotate(nums)
        if(nums[k] == target):
            return k
        temp1 = bSearch(nums,0,k-1,target)
        if(temp1!=-1):
            return temp1
        temp2 = bSearch(nums,k+1,n-1,target)
        if(temp2!=-1):
            return temp2
        return -1
        