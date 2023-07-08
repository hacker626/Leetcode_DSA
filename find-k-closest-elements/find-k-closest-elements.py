import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # low,high = 0,len(arr)
        # while(high-low>k):
        #     if(x-arr[low]>arr[high-1]-x):
        #         low+=1
        #     else:
        #         high-=1
        # return arr[low:high]
        # # ffffffxx
        maxHeap = []

        for i in range(len(arr)):
            heapq.heappush(maxHeap,[-abs(x-arr[i]),-arr[i],arr[i]])
            if(len(maxHeap)>k):
                heapq.heappop(maxHeap)
        ans = []
        while(len(maxHeap)>0):
            res = heapq.heappop(maxHeap)
            ans.append(res[2])
        return sorted(ans)