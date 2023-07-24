class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        row = len(mat)
        col = len(mat[0])
        if(row == col == 1):
            return [0,0]
        elif(row>=2 and col>=2):
            if(mat[0][0]>mat[0][1] and mat[0][0]>mat[1][0]):
                return [0,0]
            elif(mat[0][col-1]>mat[0][col-2] and mat[0][col-1]>mat[1][col-1]):
                return [0,col-1]
            elif(mat[row-1][0]>mat[row-2][0] and mat[row-1][0]>mat[row-1][1]):
                return [row-1,0]
            elif(mat[row-1][col-1]>mat[row-1][col-2] and mat[row-1][col-1]>mat[row-2][col-1]):
                return [row-1,col-1]
        
        for i in range(len(mat)):
            n = len(mat[i])
            low,high = 0,n-1
            # if(n == )
            while(low<=high):
                mid = low+(high-low)//2
                if(n-1>mid>0 and mat[i][mid]<mat[i][mid-1] and mat[i][mid-1]>mat[i][mid+1]):
                    high=mid-1
                    continue
                if(n-1>mid>0 and mat[i][mid]<mat[i][mid+1] and mat[i][mid-1]<mat[i][mid+1]):
                    low=mid+1
                    continue
                
                if(mid>0 and mat[i][mid]<mat[i][mid-1]):
                    high=mid-1
                    continue
                if(mid<n-1 and mat[i][mid]<mat[i][mid+1]):
                    low=mid+1
                    continue
                if(i>0 and mat[i][mid]<mat[i-1][mid]):
                    break
                if(i<row-1 and mat[i][mid]<mat[i+1][mid]):
                    break
                return [i,mid]
            


        # print(mat)
        # return [0,1]