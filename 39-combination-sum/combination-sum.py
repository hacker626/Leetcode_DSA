class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # dp = {}
        arr = []
        self.func(candidates,target,{},len(candidates),arr,[])
        return arr
        
    def func(self,arr,target,dp,n,ans,temp):
        if(target == 0):
            ans.append(temp[:])
            return
        elif(target<0 or n<=0):
            return 



       
        if(target-arr[n-1]>=0):
            self.func(arr,target-arr[n-1],dp,n,ans,temp+[arr[n-1]])
        self.func(arr,target,dp,n-1,ans,temp)
        
        