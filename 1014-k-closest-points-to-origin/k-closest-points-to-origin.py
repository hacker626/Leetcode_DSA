import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        maxHeap = []
        for i in range(len(points)):
            distOrigin = (points[i][1]**2+points[i][0]**2)
            heapq.heappush(maxHeap,[-distOrigin,points[i]])
            if(len(maxHeap)>k):
                heapq.heappop(maxHeap)
        return [i[1] for i in maxHeap]
