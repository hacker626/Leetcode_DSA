class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        maxNum = arr[0]
        i = 1
        while(len(arr)>=2):
            if(arr[1]<maxNum):
                count+=1
                arr.pop(1)
                
            else:
                arr.pop(0)
                count = 1
                maxNum = arr[0]
            if(count == k):
                    return maxNum
            i+=1
        return maxNum

        