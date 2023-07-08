import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxHeap = []
        for i in range(len(arr)):
            heapq.heappush(maxHeap,[-abs(x-arr[i]),-arr[i],arr[i]])
            # print(maxHeap)
            if(len(maxHeap)>k):
                heapq.heappop(maxHeap)
                # print("Popped: ",maxHeap)
        # dict_ = {}
        # print(maxHeap)
        ans = []
        for i in maxHeap:
            ans.append(i[2])
        return sorted(ans)
        # while(len(maxHeap)>0):
        #     temp = heapq.heappop(maxHeap)
        #     if(temp not in dict_):
        #         dict_[temp] = 1
        #     else:
        #         dict_[temp] += 1
        # print(dict_)
        # ans = []
        # for i in dict_:
        #     if(dict_[i] == 1):
        #         ans.append(x+abs(i))
        #     else:
        #         ans+=[x+abs(i),x-abs(i)]
        
        # return sorted(ans)
        # print(maxHeap)