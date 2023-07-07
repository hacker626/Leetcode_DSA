class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i,j = 0,0

        ans = 0
        dict_ = {'T':0,'F':0}
        while(j<len(answerKey)):
            dict_[answerKey[j]] +=1
            # ans = max(ans,dict_['T']+dict_['F'])
            while(dict_['T']>k and dict_['F']>k):
                dict_[answerKey[i]]-=1
                i+=1
            ans = max(ans,dict_['T']+dict_['F'])

                
            j+=1
        return ans


