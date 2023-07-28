import math
class Solution(object):
    def minSpeedOnTime(self, dist, hour):
 
        low,high = 1,10**7
        finalAns = -1

        while(low<=high):
            
            mid = low+(high-low)//2

            tempSum = 0.0
            for i in range(len(dist)-1):
                tempSum += math.ceil(float(dist[i])/float(mid))
            tempSum+=(float(dist[-1])/float(mid))
            if(tempSum<=hour):
                finalAns = mid
                high = mid-1
            else:
                low = mid+1
        return finalAns



        