class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row=len(matrix)
        col = len(matrix[0])

        low,high=0,(row*col)-1

        while(low<=high):
            mid=low+(high-low)//2

            if(matrix[mid//col][mid%col] == target):
                return 1
            elif(matrix[mid//col][mid%col]>target):
                high=mid-1
            else:
                low=mid+1
        return 0
        