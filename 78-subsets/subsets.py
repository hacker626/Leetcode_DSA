class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        dict_ = []
        temp = len(nums)
        print(temp)
        self.func(nums,dict_,temp,[])
        return dict_
    def func(self,nums,dict_,n,ans):
        if(n<=0):
            dict_.append(ans)
            return       



        self.func(nums,dict_,n-1,ans)
        temp = ans+[nums[n-1]]
        # print(temp)
        self.func(nums,dict_,n-1,temp)


        