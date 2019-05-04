class Solution:
    def isVowel(self, s: str) -> bool:
        if s == 'u' or s == 'U':
            return True
        elif s == 'e' or s == 'E':
            return True
        elif s == 'o' or s == 'O':
            return True
        elif s == 'a' or s == 'A':
            return True
        elif s == 'i' or s == 'I':
            return True

        return False

    def reverseVowels(self, s: str) -> str:
        sList = []
        n = len(s)
        for i in range(n):
            sList.append(s[i])

        vowelsList = []
        for i in range(n):
            if self.isVowel(sList[i]):
                vowelsList.append(sList[i])
                sList[i] = None

        vowelsList.reverse()

        for i in range(n):
            if sList[i] == None:
                sList[i] = vowelsList.pop(0)

        return ''.join(sList)