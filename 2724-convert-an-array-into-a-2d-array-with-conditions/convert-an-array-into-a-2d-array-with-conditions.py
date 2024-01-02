class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dict_ = {}
        for i in range(len(nums)):
            if(nums[i] not in dict_):
                dict_[nums[i]] = 1
            else:
                dict_[nums[i]] += 1
        
        ans = []
        for i in dict_:
            temp = dict_[i]
            j = 0
            while(j<temp):
                if(j>=len(ans)):
                    ans.append([i])
                else:
                    ans[j].append(i)

                j+=1
        return ans
                
        