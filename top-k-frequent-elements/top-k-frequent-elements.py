import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = {}
        for i in nums:
            if(i not in dict_):
                dict_[i] = 1
            else:
                dict_[i] += 1
        minHeap = []
        for i in dict_:
            heapq.heappush(minHeap,[dict_[i],i])
            if(len(minHeap)>k):
                heapq.heappop(minHeap)
        return [i[1] for i in minHeap]