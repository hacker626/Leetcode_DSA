class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        cr = len(mat)
        cc = len(mat[0])
        if(r*c != cr*cc):
            return mat
        newArr = [[-1 for i in range(c)] for j in range(r)]
        nr,nc=0,0
        for i in mat:
            for j in i:
                newArr[nr][nc] = j
                nc+=1
                if(nc>=c):
                    nc=0
                    nr+=1
        return newArr