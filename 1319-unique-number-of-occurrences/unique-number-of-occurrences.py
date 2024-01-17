class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict_ = {}
        for i in arr:
            if(i not in dict_):
                dict_[i] = 1
            else:
                dict_[i] += 1
        
        dict2 = {}
        for j in list(dict_.values()):
            if(j not in dict2):
                dict2[j] = 1
            else:
                return 0
        return 1
        