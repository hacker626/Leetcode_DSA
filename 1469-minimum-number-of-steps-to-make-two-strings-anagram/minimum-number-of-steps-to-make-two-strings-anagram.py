class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """    
        dict_s = {}
        dict_t = {}
        count = 0
        for i in s:
            if(i not in dict_s):
                dict_s[i]  = 1
            else:
                dict_s[i]+=1
        for j in t:
            if(j in dict_s and dict_s[j]>0):
                dict_s[j]-=1
            else:
                count+=1
        return count
        