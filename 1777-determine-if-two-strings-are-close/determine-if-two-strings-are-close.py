class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        dict1 = {}
        dict2 = {}
        # return len(word2) == len(word1)
        for i in word1:
            if(i not in dict1):
                dict1[i] = 1
            # else:
            #     dict1[i] += 1
        # print(dict1)
        for j in word2:
            # print(j,dict1)
            if(j not in dict2):
                dict2[j] = 1
                # if(dict1[j]<=0):
                #     return 0
                # else:
                #     dict1[j]-=1
            # else:
            #     return 0
                # dict2[i] += 1
        # print(dict1,/dict2)
        # return len(word1) == len(word2) and (dict1 == dict2)
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
        
        


        