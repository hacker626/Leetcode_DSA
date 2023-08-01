class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        stack = []
        ans = []

        for i in range(len(temperatures)-1,-1,-1):

            while(len(stack)>0 and temperatures[stack[-1]]<=temperatures[i]):
                stack.pop()
            
            if(len(stack) == 0):
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(i)
        ans.reverse()
        # print(ans)

        for i in range(len(temperatures)):
            if(ans[i] != -1):
                ans[i] = ans[i]-i
            else:
                ans[i] = 0
        return ans

        