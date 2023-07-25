class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """


        stack = []
        ansL = []
        for i in range(len(heights)):
            while(len(stack)>0 and heights[stack[-1]]>=heights[i]):
                stack.pop()
            
            
            if(len(stack) == 0):
                ansL.append(-1)
            else:
                ansL.append(stack[-1])

            stack.append(i)
        stack1 = []
        ansL1 = []
        for i in range(len(heights)-1,-1,-1):
            while(len(stack1)>0 and heights[stack1[-1]]>=heights[i]):
                stack1.pop()
            
            
            if(len(stack1) == 0):
                ansL1.append(len(heights))
            else:
                ansL1.append(stack1[-1])

            stack1.append(i)
        
        ansL1.reverse()
        finalAns = float('-inf')
        # print(ansL,ansL1)

        for i in range(len(heights)):
            right=ansL1[i]-1
            left=ansL[i]+1
            finalAns=max(finalAns,heights[i]*(right-left+1))
        return finalAns
