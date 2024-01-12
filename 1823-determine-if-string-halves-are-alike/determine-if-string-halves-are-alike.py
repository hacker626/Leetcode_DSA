class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        halflen = len(s)//2
        count = {"a":0,"e":0,"i":0,"o":0,"u":0,"A":0,"E":0,"I":0,"O":0,"U":0}
        temp = 0
        for i in range(len(s)):
            if(s[i] in count):
                if(i<halflen):
                    temp+=1
                else:
                    temp-=1
        # print(count)
        return temp == 0

            
        
        