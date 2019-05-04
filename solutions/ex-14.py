class Solution:
    def str2list(self, s: str) -> List[str]:
        sList = []
        for i in range(len(s)):
            sList.append(s[i])
        return sList

    def delCharsByBackspace(self, s: List[str]):
        numBackspace = 0
        index = len(s) - 1
        while index >= 0:
            if s[index] == '#':
                numBackspace += 1
                index = index - 1
            else:
                if numBackspace > 0:
                    s.pop(index)
                    numBackspace -= 1
                    index = index - 1
                else:
                    index = index - 1
        i = 0
        while i < len(s):
            if s[i] == '#':
                s.pop(i)
            else:
                i = i + 1
        return s

    def backspaceCompare(self, S: str, T: str) -> bool:
        sList = self.str2list(S)
        tList = self.str2list(T)

        self.delCharsByBackspace(sList)
        self.delCharsByBackspace(tList)

        if ''.join(sList) == ''.join(tList):
            return True

        return False