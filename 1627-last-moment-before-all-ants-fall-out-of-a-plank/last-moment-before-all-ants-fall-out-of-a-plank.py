class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        right+=[float('inf')]
        temp1 = n-min(right)

        left+=[0]
        temp2 = max(left)
        return max(temp1,temp2)