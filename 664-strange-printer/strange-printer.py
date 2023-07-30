class Solution:
    def strangePrinter(self, s):
        memo = {}
        def check(i, j,s):
            if (i, j) not in memo:
                if i > j: return 0
                
                res = check(i, j-1,s) + 1
                for k in range(i, j):
                    if s[k] == s[j]:
                        res = min(res, check(i, k-1,s) + check(k, j-1,s))
                memo[(i, j)] = res
                
            return memo[(i, j)]
        
        temp = [0]
        ans = ""
        i = 0
        while(i<len(s)):
            ans+=s[i]
            temp[0] = s[i]
            i+=1
            while(i<len(s) and temp[0] == s[i]):
                i+=1
            temp[0] = 0
            
        # print(ans)
        return check(0, len(ans) - 1,ans)
