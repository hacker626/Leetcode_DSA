class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)
        low = 0
        high = n-1
        def binaryS(nums,s,e):

            while(s<=e):
                mid = s+(e-s)//2
                if(nums[mid] == target):
                    return mid
                elif(nums[mid]>target):
                    e=mid-1
                else:
                    s=mid+1
            return float('inf')
        def rotate(nums):
            low,high=0,n-1
            if(nums[0]<nums[-1]):
                return 0
            
            while(low<=high):
                mid=(low)+(high-low)//2

                if(0<mid<n-1 and nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]):
                    return mid
                elif(nums[mid]<nums[-1]):
                    high=mid-1
                else:
                    low=mid+1
            return n-1

        k = rotate(nums)

        if(nums[k] == target):
            return k
        temp1=binaryS(nums,0,k-1)
        if(temp1 !=float('inf')):
            return temp1
        

        temp2 = binaryS(nums,k+1,n-1)
        if(temp2 !=float('inf')):
            return temp2
        return -1


        