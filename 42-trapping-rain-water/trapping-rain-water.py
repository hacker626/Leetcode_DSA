class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        Mridul Bhaskar
        """
        low = 0
        high = len(height)-1
        ans = 0
        temp = 0


        while(low<=high):
            if(height[low]<height[high]):

                temp = max(temp,height[low])
                ans+=(temp-height[low])
                low+=1
            else:
                temp = max(temp,height[high])
                ans+=(temp-height[high])
                high-=1
        return ans
