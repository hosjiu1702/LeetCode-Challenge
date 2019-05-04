class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sList = []
        for i in range(len(S)):
            sList.append(S[i])
        
        ret = 0
        for i in range(len(J)):
            index = 0
            while index < len(sList):
                if sList[index] == J[i]:
                    ret = ret + 1
                    sList.pop(index)
                else:
                    index = index + 1
                    
        return ret