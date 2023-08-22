class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ans = ""
        while(columnNumber>0):
            columnNumber-=1
            ans+=chr(65+(columnNumber)%26)
            columnNumber//=26
        return ans[::-1]
# (ans[::-1])