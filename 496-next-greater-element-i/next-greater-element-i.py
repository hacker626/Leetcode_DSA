class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = []
        for i in range(len(nums2)-1,-1,-1):
            if(len(stack)>0):
                if(stack[-1]<nums2[i]):
                    while(len(stack)>0 and stack[-1]<nums2[i]):
                        stack.pop()
                if(len(stack)>0):
                    ans.append(stack[-1])
                else:
                    ans.append(-1)
                stack.append(nums2[i])
                pass
            else:
                stack.append(nums2[i])
                ans.append(-1)
        
        ans.reverse()
        print(ans)
        dict_ = {}
        # finalAns = []
        for i in range(len(nums2)):
            dict_[nums2[i]] = i
        finalAns = []
        for i in nums1:
            finalAns.append(ans[dict_[i]])
        return finalAns

            
        