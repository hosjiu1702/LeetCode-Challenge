class Solution:
    def __init__(self):
        self.mapTable = {
            "q": 1,
            "w": 2,
            "e": 3,
            "r": 4,
            "t": 5,
            "y": 6,
            "u": 7,
            "i": 8,
            "o": 9,
            "p": 10,
            "a": 11,
            "s": 12,
            "d": 13,
            "f": 14,
            "g": 15,
            "h": 16,
            "j": 17,
            "k": 18,
            "l": 19,
            "z": 20,
            "x": 21,
            "c": 22,
            "v": 23,
            "b": 24,
            "n": 25,
            "m": 26
        }

    def getRow(self, char: str) -> int:
        if self.mapTable[char] <= self.mapTable['p']:
            return 3
        elif self.mapTable[char] <= self.mapTable['l']:
            return 2
        return 1

    def isSameRow(self, char1: str, char2: str) -> bool:
        if self.getRow(char1) == self.getRow(char2):
            return True
        return False

    def findWords(self, words: List[str]) -> List[str]:
        ret = []

        for word in words:
            i = 0
            sameRow = True
            while i < len(word) - 1:
                if not self.isSameRow(word[i].lower(), word[i + 1].lower()):
                    sameRow = False
                    break
                i = i + 1
            if sameRow:
                ret.append(word)

        return ret