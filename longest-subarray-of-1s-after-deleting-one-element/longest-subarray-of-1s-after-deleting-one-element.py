class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt,prvCnt = 0,0
        res = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                cnt+=1
            else:
                res = max(res,cnt+prvCnt)
                prvCnt = cnt
                cnt =  0
        
        ans = max(res,cnt+prvCnt)
        return ans-1 if(ans == len(nums)) else ans

        # low,high = 0,0
        # index0 = 0
        # ans = float('-inf')
        # while(high<len(nums)):
        #     if(nums[high] == 0):
        #         index0+=1
        #     if(index0 == 2):
        #         ans = max(ans,high-low-1)
        #         while(nums[low] != 0):
        #             low+=1
        #         low+=1
        #         index0-=1
        #     high+=1
        # return max(ans,high-low-1)

                    