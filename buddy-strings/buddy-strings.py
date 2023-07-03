class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        store = []
        dict_ = {}
        for i in range(len(s)):
            if(s[i] not in dict_):
                dict_[s[i]] = 1
            else:
                dict_[s[i]] += 1
            if(s[i] != goal[i]):
                store.append(i)
        if(s == goal):
            for i in dict_:
                if(dict_[i]>=2):
                    return 1
        # print(store)
        if(len(store)>0 and (s[store[0]] != goal[store[-1]] or s[store[-1]] != goal[store[0]])):
            return 0
        return (len(store) == 2 and (len(s) == len(goal)))