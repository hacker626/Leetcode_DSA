class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if(n == 0):
            return 1
        temp = self.myPow(x,abs(n)//2)
        temp*=temp
        if(abs(n)%2!=0):
            temp*=x
        return temp if(n>=0) else 1/temp

        