class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row,col = len(matrix),len(matrix[0])

        l,r = 0,(row*col)-1

        while(l<=r):
            mid = l+(r-l)//2
            if(matrix[mid//col][mid%col] == target):
                return 1
            elif(matrix[mid//col][mid%col]<target):
                l = mid+1
            else:
                r=mid-1
        return 0

        