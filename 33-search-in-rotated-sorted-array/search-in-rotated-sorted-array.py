class Solution(object):
    def binarySearch(self,arr,low,high,target):

        while(low<=high):
            mid = low+(high-low)//2
            if(arr[mid] == target):
                return mid
            elif(arr[mid]>target):
                high=mid-1
            else:
                low=mid+1
        return -1
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low,high = 0,len(nums)-1
        index = self.findIndex(nums,low,high)
        # print(index)
        tempo = self.binarySearch(nums,0,index-1,target)

        if(tempo!=-1):
            return tempo
        tempo2 = self.binarySearch(nums,index,high,target)
        # print(tempo,tempo2)
        if(tempo2!=-1):
            return tempo2
        return -1




    def findIndex(self,nums,low,high):

        if(nums[0]<=nums[-1]):
            return 0
        low,high = 0,len(nums)-1
        while(low<=high):
            mid = low+(high-low)//2
            if(0<mid<len(nums)-1 and nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]):
                return mid
            elif(nums[mid]<nums[-1]):
                high=mid-1
            else:
                low=mid+1
        return high

        