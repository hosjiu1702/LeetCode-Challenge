class Solution:
    def isAlphabet(self, c: str) -> bool:
        if ord(c) <= 122 and ord(c) >= 97:
            return True
        elif ord(c) <= 90 and ord(c) >= 65:
            return True
        return False
    
    def reverseOnlyLetters(self, S: str) -> str:
        sList = []
        for i in range(len(S)):
            sList.append(S[i])

        temp = []
        for i in range(len(sList)):
            if self.isAlphabet(sList[i]):
                temp.append(sList[i])
                sList[i] = None

        temp.reverse()

        for i in range(len(sList)):
            if sList[i] == None:
                sList[i] = temp.pop(0)

        return ''.join(sList)