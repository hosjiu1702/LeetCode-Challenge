class Solution:
    def isSameType(self, openBracket: str, closeBracket: str):
        if ord(closeBracket) - ord(openBracket) == 1:
            return True
        elif ord(closeBracket) - ord(openBracket) == 2:
            return True
        return False

    def isOpenBracket(self, bracket: str) -> bool:
        if ord(bracket) == 40:
            return True
        elif ord(bracket) == 91:
            return True
        elif ord(bracket) == 123:
            return True
        return False

    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False

        openBracketsList = []
        index = 0
        while index < n:
            if self.isOpenBracket(s[index]):
                openBracketsList.append(s[index])
                index = index + 1
            else:
                if len(openBracketsList) == 0:
                    return False
                else:
                    latestOpenBracket = openBracketsList.pop(-1)
                    currentCloseBracket = s[index]
                    if not self.isSameType(latestOpenBracket, currentCloseBracket):
                        return False
                    else:
                        index = index + 1

        if len(openBracketsList) != 0:
            return False

        return True