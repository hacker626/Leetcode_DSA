from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)

        def func(S):

            if(S == ""):
                return True
            
            for i in wordDict:
                if S.startswith(i):
                    temp = len(i)
                
                    if(func(S[temp:])):
                        return True
            return False
        return func(s)

# from functools import lru_cache #added this
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         @lru_cache(None) # and this
#         def helper(prev):
#             if prev=="":return True
#             for word in wordDict:
#                 if prev.startswith(word):
#                     i=len(word)
#                     if helper(prev[i:]):return True
#             return False
#         return helper(s)