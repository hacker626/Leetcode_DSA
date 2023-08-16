class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        low,high = 0,0
        maxNum = []
        ans = []
        while(high<len(nums)):
            #here maxNum[-1]<=nums[high] cannot be taken because if considered like this then we will pop out the old num[high] if repitition caused and it will ultimately deletes out the remaining nums[high] if windows slides forward.
            #here 7 is maximum in slides for example [-7,-8,7,5,7,1,6,0] if second 7 is encoutered we are gonna deleting the old one, and when windows slides forwards; we have to delete out the maximum element which is 7.It means both the 7 will be delete out.
            #Therefore ensure that the leftmost element of maxNum is maximum and leftmost in nums.
            while(len(maxNum)>0 and maxNum[-1]<nums[high]):
                maxNum.pop()
            maxNum.append(nums[high])
            if(high-low+1 == k):
                ans.append(maxNum[0])
                if(maxNum[0] == nums[low]):
                    maxNum.pop(0)
                low+=1
            high+=1
        return ans

        