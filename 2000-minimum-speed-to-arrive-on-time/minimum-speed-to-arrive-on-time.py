import math

class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        low,high = 1,10**7
        ans = -1

        while(low<=high):
            mid = low+(high-low)//2
            temp = 0.0
            for i in range(len(dist)-1):
                temp = math.ceil(temp + float(dist[i]/float(mid)))
                # if(mid == 3):
                #     print(temp)
                # return mid
            temp+=(float(dist[-1]/float(mid)))
            if(temp>hour):
                low = mid+1
            else:
                ans = mid
                high = mid-1
        return ans