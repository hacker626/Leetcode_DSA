class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # return 1 if

        return 1 if(self.solve(n,k)) else 0

    def solve(self,n,k):

        if(n == 1 and k == 1):
            return 0
        if(k<=(2**(n-2))):
            return self.solve(n-1,k)
        else:
            return not self.solve(n-1,k-(2**(n-2)))

        

