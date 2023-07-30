class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        temp = {}
        self.func(s,temp,len(s))
        return temp.keys()


    def func(self,s,temp,n):


        if(n == 0):
            if(s not in temp):
                temp[s] = 1
            return
        # str1 = s
        
        if(65<=ord(s[n-1])<=90):
            str1 = s[:n-1]+s[n-1].lower()+s[n:]
            self.func(str1,temp,n-1)
        elif(97<=ord(s[n-1])<=122):
            str1 = s[:n-1]+s[n-1].upper()+s[n:]
            self.func(str1,temp,n-1)
        # if(n == 1):
        #     print(str1)
        
        # if(str1 not in temp):
        #     temp[str1] = 1
        self.func(s,temp,n-1)
        
        
        