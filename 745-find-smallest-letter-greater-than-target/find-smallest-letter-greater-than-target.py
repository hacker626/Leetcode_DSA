class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        ans = -1

        low,high = 0,len(letters)-1


        while(low<=high):
            mid = low+(high-low)//2

            if(ord(letters[mid])>ord(target)):
                ans = letters[mid]
                high = mid-1
            else:
                low = mid+1
        return letters[0] if (ans == -1) else ans































        
        # if(ord(letters[0])>ord(target) or ord(letters[-1])<=ord(target)):
        #     return letters[0]
        
        
        
        # for i in letters:
        #     if(ord(i)>ord(target)):
        #         return (i)
                
                    
                
        