class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binNum = bin(n)
        i = 2
        while i < len(binNum) - 1:
            if binNum[i] != binNum[i + 1]:
                i = i + 1
            else:
                return False

        return True