class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dict_ = {}
        ans = -1

        for i in range(len(s)):
            if(s[i] not in dict_):
                dict_[s[i]] = i
            else:
                ans = max(ans,i-dict_[s[i]]-1)
        return ans
        



        