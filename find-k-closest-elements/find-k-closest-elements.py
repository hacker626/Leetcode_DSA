import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxHeap = []
        for i in range(len(arr)):
            heapq.heappush(maxHeap,[-abs(x-arr[i]),-arr[i],arr[i]])
            if(len(maxHeap)>k):
                heapq.heappop(maxHeap)

        ans = []
        for i in maxHeap:
            ans.append(i[2])
        return sorted(ans)
