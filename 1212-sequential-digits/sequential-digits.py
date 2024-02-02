class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        # start with 1,2,3,4,5,6,7,8,9
        ans = []
        for i in range(1,9):
            num = i
            next = i+1
            
            while(next<=9 and num<=10**9):
                num = num*10+next
                if(low<=num<=high):
                    ans.append(num)
                next+=1
        return sorted(ans)
        
