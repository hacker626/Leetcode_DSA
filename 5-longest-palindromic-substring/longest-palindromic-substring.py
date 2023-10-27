class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for i in range(len(s)):
            temp = self.func(i,i,s)
            if(len(temp)>len(ans)):
                ans = temp




            temp2 = self.func(i,i+1,s)
            if(len(temp2)>len(ans)):
                ans = temp2
        return ans
    def func(self,i,j,s):


        while(i>=0 and j<len(s) and s[i] == s[j]):
            i-=1
            j+=1
        return s[i+1:j]

            



        