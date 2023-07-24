class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])

        i,j=row-1,0

        while(0<=i<row and 0<=j<col):
            if(matrix[i][j] == target):
                return 1
            elif(matrix[i][j]>target):
                i-=1
            else:
                j+=1
        return 0