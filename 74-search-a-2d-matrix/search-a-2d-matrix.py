class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row,col = 0,len(matrix[0])-1

        while(0<=row<len(matrix) and 0<=col<len(matrix[0])):

            if(target == matrix[row][col]):
                return 1
            elif(target>matrix[row][col]):
                row+=1
            else:
                col-=1
        return 0
        