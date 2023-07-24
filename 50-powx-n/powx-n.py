class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # return x**n
        # if(n == 0):
        #     return 1
        # temp = self.myPow(x*x,abs(n)//2)
        # if(abs(n)%2 !=0):
        #     temp*=x
        # return float(temp) if(n>=0) else float(1/temp)
        if(n == 0):
            return 1
        temp = self.myPow(x,(abs(n)//2))
        temp*=temp
        if(abs(n)%2 != 0):
            temp*=x 
        return float(temp) if(n>=0) else float(1/temp)