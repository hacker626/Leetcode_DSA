import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low,high = 0,len(arr)
        while(high-low>k):
            if(x-arr[low]>arr[high-1]-x):
                low+=1
            else:
                high-=1
        return arr[low:high]
        # ffffff