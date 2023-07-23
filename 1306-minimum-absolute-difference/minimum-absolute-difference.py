class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """

        arr.sort()
        minDiff = float('inf')
        for i in range(1,len(arr)):
            if((arr[i]-arr[i-1])<minDiff):
                minDiff = arr[i]-arr[i-1]
        ans = []
        for i in range(1,len(arr)):
            if((arr[i]-arr[i-1]) == minDiff):
                ans.append([arr[i-1],arr[i]])
        return ans