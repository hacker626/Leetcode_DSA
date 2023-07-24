class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # return x**n
        tempo = n
        n=abs(n)
        if(n == 0):
            return 1
        temp = self.myPow(x*x,(n//2))
        if(n%2 != 0):
            temp*=x 
        return float(temp) if(tempo>=0) else float(1/temp)