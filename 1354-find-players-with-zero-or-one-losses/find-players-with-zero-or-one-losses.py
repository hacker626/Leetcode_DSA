class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        dict_ = {}
        count_1 = {}
        ans = [[],[]]
        for i in matches:
            for j in i:
                if(j not in dict_):
                    dict_[j] = 1
            if(i[1] not in count_1):
                count_1[i[1]] = 1
            else:
                count_1[i[1]]+=1

        # players = dict_.keys()
        # print(players)

        for i in dict_:
            if(i not in count_1):
                ans[0].append(i)
            elif(count_1[i] == 1):
                ans[1].append(i)
        ans[0] = sorted(ans[0])
        ans[1] = sorted(ans[1])
        return ans

        
        
        