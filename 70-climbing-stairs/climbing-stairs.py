class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        arr = [-1 for i in range(n+1)]
        return self.func(arr,n)


    def func(self,arr,n):

        if(n == 0 or n == 1):
            return 1
        if(arr[n]!=-1):
            return arr[n]
        # elif(n == 0):
        #     return 0
        arr[n] = self.func(arr,n-1)+self.func(arr,n-2)
        return arr[n]