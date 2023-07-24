# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def binarySearch(self,arr,low,high,target):

        while(low<=high):
            mid = low+(high-low)//2
            if(arr.get(mid) == target):
                return mid
            elif(arr.get(mid)>target):
                high=mid-1
            else:
                low=mid+1
        return -1
    def binary2Search(self,arr,low,high,target):

        while(low<=high):
            mid = low+(high-low)//2
            if(arr.get(mid) == target):
                return mid
            elif(arr.get(mid)>target):
                low=mid+1
                
            else:
                high=mid-1
                
        return -1
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        n = mountain_arr.length()
        low,high = 0,n-1
        index = 0


        while(low<=high):
            mid = low+(high-low)//2
            if(0<=mid+1<n):
                sE = mountain_arr.get(mid+1)
            if(0<=mid<n):
                sM = mountain_arr.get(mid)
            if(0<=mid-1<n):
                sB = mountain_arr.get(mid-1)


            if(0<mid<n-1 and sM>sE and sM>sB):
                if(sM == target):
                    return mid
                index = mid
                break
            elif(mid<n-1 and sM>sE):
                high=mid-1
            else:
                low=mid+1
        # print(index)
        temp1 = self.binarySearch(mountain_arr,0,index,target)
        if(temp1!=-1):
            return temp1
        # print(index+1,n-1,_arr)
        temp2 = self.binary2Search(mountain_arr,index+1,n-1,target)
        if(temp2!=-1):
            return temp2
        return -1



