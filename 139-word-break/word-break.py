from functools import lru_cache #added this
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None) # and this
        def helper(prev):
            if prev=="":return True
            cur=prev
            for word in wordDict:
                if prev.startswith(word):
                    i=len(word)
                    if helper(prev[i:]):return True
            return False
        return helper(s)