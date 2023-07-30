class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dict_ = []
        self.func(nums,dict_,0,[])
        return list(dict_)

    def func(self,nums,dict_,n,ans):
        if(n == len(nums)):
            dict_.append(ans)
            return
        # ans.append()
        self.func(nums,dict_,n+1,ans)
        temp = ans+[nums[n]]
        # ans.append(nums[n])
        self.func(nums,dict_,n+1,temp)
        # ans.pop()
        
        