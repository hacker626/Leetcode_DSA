import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for i in points:
            dist = (i[0]**2+i[1]**2)**(0.5)
            heapq.heappush(maxHeap,[-dist,i])
            if(len(maxHeap)>k):
                heapq.heappop(maxHeap)
        return [i[1] for i in maxHeap]