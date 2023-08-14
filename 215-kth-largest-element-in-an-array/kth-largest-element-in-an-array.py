import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        temp = []

        for i in range(len(nums)):
            heapq.heappush(temp,nums[i])
            if(len(temp)>k):
                heapq.heappop(temp)
        return temp[0]