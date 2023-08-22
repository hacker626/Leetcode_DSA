# class Solution(object):
#     def convertToTitle(self, columnNumber):
#         """
#         :type columnNumber: int
#         :rtype: str
#         """
#         ans = ""
#         while(columnNumber>0):
#             if(columnNumber%26 == 0):
#                 ans+="Z"
#                 ans
#                 break
#             ans+=chr(65+columnNumber%26-1)
#             columnNumber//=26
#         return ans[::-1]
class Solution:
    def convertToTitle(self, n):
        ans = []
        while(n > 0):
            n -= 1
            curr = n % 26
            n = int(n / 26)
            ans.append(chr(curr + ord('A')))
            # print(ans,curr)
        
        return ''.join(ans[::-1])