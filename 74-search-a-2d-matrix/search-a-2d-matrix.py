class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        low,high = 0,len(matrix[0])*len(matrix)-1

        while(low<=high):
            mid = (low)+(high-low)//2
            ar = mid//len(matrix[0])
            ac = mid%len(matrix[0])
            if(matrix[ar][ac] == target):
                return 1
            elif(matrix[ar][ac]>target):
                high = mid-1
            else:
                low = mid+1
        return 0
