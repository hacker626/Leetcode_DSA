class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dict_ = [0]*26
        for i in words:
            for j in i:
                temp = ord(j)-97
                dict_[temp]+=1
        # print(dict_)
        for i in range(26):
            if(dict_[i]%len(words) != 0):
                return 0
        return 1
        