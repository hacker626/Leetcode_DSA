class Solution(object):
    def __init__(self):
        self.dict_ = {}
    def funcsum(self,count):
        if(count == 0):
            return 0
        if(count in self.dict_):
            return self.dict_[count]
        self.dict_[count] =  (count+self.funcsum(count-1))%(10**9+7)
        return self.dict_[count]
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = -1
        count = 0
        ans = 0
        for i in range(len(s)):
            if(s[i] == prev):
                count+=1
            else:
                ans+=self.funcsum(count)
                print(ans)
                prev = s[i]
                count = 1
        return ans+self.funcsum(count)


        