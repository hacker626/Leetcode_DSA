class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """



        dict_ = {}
        self.func(s,dict_,len(s))
        return dict_.keys()

    def func(self,s,dict_,n):
        if(n<=0):
            dict_[s] = 1
            return

        if(97<=ord(s[n-1])<=122):
            temp = s[:n-1]+s[n-1].upper()+s[n:]
            self.func(temp,dict_,n-1)
        elif(65<=ord(s[n-1])<=90):
            temp = s[:n-1]+s[n-1].lower()+s[n:]
            self.func(temp,dict_,n-1)

        self.func(s,dict_,n-1)




        