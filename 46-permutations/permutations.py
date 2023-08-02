class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = []
        self.func(nums,ans,len(nums),[])
        return ans


    def func(self,nums,ans,n,temp):

        if(len(temp) ==n):
            ans.append(temp)
            return 

        for i in range(len(nums)):
            tempo = temp+[nums[i]]
            tempo2 = nums[:i]+nums[i+1:] 
            self.func(tempo2,ans,n,tempo)
        
            
        