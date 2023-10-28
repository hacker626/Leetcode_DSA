class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = [[0 for i in range(5)] for j in range(n+2)]
        
        for i in range(5):
            dp[1][i] = 1
        for i in range(2,n+1):
            dp[i][0] += dp[i-1][1]
            dp[i][1] += (dp[i-1][0]+dp[i-1][2])
            dp[i][2] += (dp[i-1][0]+dp[i-1][1]+dp[i-1][3]+dp[i-1][4])
            dp[i][3] += (dp[i-1][2]+dp[i-1][4])
            dp[i][4] += (dp[i-1][0])
        # print(dp)
        return (sum(dp[n][i] for i in range(5)))%(10**9+7)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         ans = 0
#         arr = [-1]*(n+1)
#         # temp = ['a','e','i','o','u']
#         ans = self.recMem(n,arr,[])
#         print(arr)
#         return ans%(10**9+7)
    
    
    
    
#     def recMem(self,n,arr,temp_):
#         if(n>len(arr)):
#             return 0
#         if(n == 1):
#             arr[n] = 5
#             temp_ = ['a','e','i','o','u']
#             return arr[n]
#         elif(arr[n]!=-1):
#             return arr[n]
#         if(temp_ == []):
#             self.recMem(n-1,arr,temp_)
#         temp = 0
#         for i in temp_:
#             if(i == 'a'):
#                 # temp+=self.recMem(n-1,arr,['e','i','u'])
#                 temp+=self.recMem(n+1,arr,['e'])
#             if(i == 'e'):
#                 # temp+=self.recMem(n-1,arr,['a','i'])
#                 temp+=self.recMem(n+1,arr,['a','i'])
#             if(i == 'i'):
#                 # temp+=self.recMem(n-1,arr,['e','o'])
#                 temp+=self.recMem(n+1,arr,['a','e','o','u'])
#             if(i == 'o'):
#                 # temp+=self.recMem(n-1,arr,['i'])
#                 temp+=self.recMem(n+1,arr,['i','u'])
                
#             if(i == 'u'):
#                 # temp+=self.recMem(n-1,arr,['i','o'])
#                 temp+=self.recMem(n+1,arr,['a'])
#         arr[n] = temp
#         return arr[n]
            
        

        