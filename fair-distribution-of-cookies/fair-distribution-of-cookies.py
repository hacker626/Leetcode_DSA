class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if(k == len(cookies)):
            return max(cookies)
        dp = {}
        ans = [0 for i in range(k)]
        res = [float('inf')]
        self.dfs(cookies,dp,len(cookies),k,ans,res,0)
        return res[0]
    def dfs(self,cookies,dp,n,k,ans,res,temp):
        if(n == 0):
            # print(ans,res)
            # print(temp,max(ans),ans)
            res[0] = min(res[0],temp)
            return
        for i in range(k):
            ans[i]+=cookies[n-1]
            count_ = temp
            temp = max(temp,ans[i])
            self.dfs(cookies,dp,n-1,k,ans,res,temp)
            if(temp == ans[i]):
                temp = count_
            ans[i]-=cookies[n-1]
# class Solution:
#     def distributeCookies(self, cookies: List[int], k: int) -> int:
#         dp = {}
#         ans = [0 for i in range(k)]
#         res = [float('inf')]
#         self.dfs(cookies,dp,len(cookies),k,ans,res)
#         return res[0]
#     def dfs(self,cookies,dp,n,k,ans,res):
#         if(n == 0):
#             # print(ans,res)
#             res[0] = min(res[0],max(ans))
#             return
#         for i in range(k):
#             ans[i]+=cookies[n-1]
#             self.dfs(cookies,dp,n-1,k,ans,res)
#             ans[i]-=cookies[n-1]

        