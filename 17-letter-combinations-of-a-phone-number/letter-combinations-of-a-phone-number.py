class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if(digits == ""):
            return []
        dict_ = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        ans = []
        return self.func(digits,dict_,0,"",ans)
    def func(self,digits,dict_,n,temp,ans):
        if(len(temp) == len(digits)):
            ans.append(temp)
            return
        # if(n>=len(digits)):
        #     return

        for i in dict_[int(digits[n])]:
            # tempo= temp+i
            self.func(digits,dict_,n+1,temp+i,ans)
        return ans

