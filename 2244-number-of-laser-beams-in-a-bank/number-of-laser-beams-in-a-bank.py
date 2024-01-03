class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        ans = 0
        temp = [0 for i in range(len(bank))]
        for i in range(len(bank)):
            for j in range(len(bank[i])):
                if(bank[i][j] == '1'):
                    temp[i]+=1
            # if(temp[i] == 0):
            #     temp.pop(i)
        
        # print(temp)
        tempo = []
        for i in temp:
            if(i!=0):
                tempo.append(i)
        i,j = 0,1
        while(j<len(tempo)):
            ans+=(tempo[j]*tempo[i])
            j+=1
            i+=1
        return ans
        