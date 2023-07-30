class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """



        dict_ = {}
        self.func(s,dict_,0,"")
        return dict_.keys()

    def func(self,s,dict_,n,temp):
        if(n==len(s)):
            dict_[temp] = 1
            return

        if(97<=ord(s[n])<=122):
            str1 =temp+s[n].upper()
            self.func(s,dict_,n+1,str1)
            
        elif(65<=ord(s[n])<=90):
            str1 = temp+s[n].lower()
            self.func(s,dict_,n+1,str1)
        
        temp+=s[n]
        self.func(s,dict_,n+1,temp)




        