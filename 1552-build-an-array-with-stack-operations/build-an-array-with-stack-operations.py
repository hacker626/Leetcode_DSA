class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        if(target == []):
            return []
        ans = []
        ans+=(["Push","Pop"]*(target[0]-1))
        ans+=["Push"]
        # ans = ["Push"]
        # count = 1

        for i in range(1,len(target)):
            ans+=(["Push","Pop"]*(target[i]-target[i-1]-1))
            ans.append("Push")
        return ans
        
        