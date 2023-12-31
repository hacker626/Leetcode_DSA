class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        for i in range(len(s)):
            for j in range(len(s)-1,-1,-1):
                if(s[i] == s[j]):
                    ans = max(ans,j-i-1)
                    break
        return ans
        



        