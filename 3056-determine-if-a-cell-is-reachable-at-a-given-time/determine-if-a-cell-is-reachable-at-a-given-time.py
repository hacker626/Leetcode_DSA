class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """

        
        x,y = abs(sx-fx),abs(fy-sy)
        temp = max(x,y)
        if(t<temp or (temp == 0 and (t == 1))):
            return False
        else:
            return True

        return self.func(sx,sy,fx,fy,t)




#         x,y = abs(sx-fx),abs(sy-fy)
#         maxNum = max(x,y)
#         if(maxNum>t or (maxNum == 0 and (t == 1))):
#             return False
#         else:
#             return True
#         # s = abs(fx-fy)+abs(fy-sy)
#         # if(s>t):
#         #     return True
#         # if((t-s)%2 == 0):
#         #     return True
#         # return False
# #         dp = {}
# #         temp = min(self.func(sx,sy,fx,fy,t,dp),self.func(fx,fy,sx,sy,t,{}))
# #         print(temp)
# #         if(temp<=t):
# #             return 1
# #         return 0
# #     def func(self,sx,sy,fx,fy,t,dp):
        
# #         if(sx<0 or sy<0 or t<0 or sx>fx or sy>fy):
# #             return float('inf')
# #         if(sx == fx and sy == fy):
# #             return 0
        
# #         if(sx in dp):
# #             if(sy in dp[sx]):
# #                 if(t in dp[sx][sy]):
# #                     return dp[sx][sy][t]
        
# #         if(sx not in dp):
# #             dp[sx] = {}
# #         if(sy not in dp[sx]):
# #             dp[sx][sy] = {}
        
# #         dp[sx][sy][t] =  1+min(self.func(sx+1,sy,fx,fy,t-1,dp), self.func(sx-1,sy,fx,fy,t-1,dp) , self.func(sx,sy+1,fx,fy,t-1,dp) , self.func(sx,sy-1,fx,fy,t-1,dp) , self.func(sx+1,sy+1,fx,fy,t-1,dp) , self.func(sx+1,sy-1,fx,fy,t-1,dp) , self.func(sx-1,sy-1,fx,fy,t-1,dp), self.func(sx-1,sy+1,fx,fy,t-1,dp))
# #         return dp[sx][sy][t]
        
        