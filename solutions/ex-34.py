class Solution:
    def delElemsFromBlackList(self, s: List[str], blackList: List[str]):
        for word in blackList:
            if word in s:
                s.remove(word)
                
    def deleteDuplicates(self, s: List[str]) -> List[str]:
        blackList = []
        
        index = 0
        while index < len(s) - 1:
            if s[index] != s[index + 1]:
                index = index + 1
            else:
                count = 1
                base = index
                blackList.append(s[base])
                while s[index] == s[index + 1]:
                    count = count + 1
                    index = index + 1
                    if index == len(s) - 1:
                        break
                for _ in range(count-1):
                    s.pop(base)
                index = base + 1
        return blackList
                
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        AList = A.split(' ')
        BList = B.split(' ')
        
        AList.sort()
        BList.sort()
        
        blackListOfA = self.deleteDuplicates(AList)
        blackListOfB = self.deleteDuplicates(BList)
        
        index = 0
        while index < len(AList):
            word = AList[index]
            if word in BList:
                BList.remove(word)
                AList.pop(index)
            else:
                index = index + 1
        
        self.delElemsFromBlackList(AList, blackListOfA)
        self.delElemsFromBlackList(BList, blackListOfB)
        
        AList[len(AList):] = BList
        
        return AList