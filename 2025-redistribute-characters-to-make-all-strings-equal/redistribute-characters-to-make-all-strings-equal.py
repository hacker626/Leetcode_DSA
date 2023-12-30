class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dict_ = {}
        for i in words:
            for j in i:
                if(j not in dict_):
                    dict_[j] = 1
                else:
                    dict_[j] += 1
        # print(dict_)
        for i in dict_:
            if(dict_[i]%len(words) != 0):
                return 0
        return 1
        