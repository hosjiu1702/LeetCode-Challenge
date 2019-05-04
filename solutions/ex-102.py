class Solution:
    def findAliquot(self, n: int) -> List[int]:
        ret = []

        if n < 2:
            return [1]

        for b in range(1, n):
            r = n % b
            if r == 0:
                q = int((n - r) / b)
                ret.append(b)
                ret.append(q)
        ret.sort()

        index = 0
        while index < len(ret) - 1:
            if ret[index] == ret[index+1]:
                ret.pop(index)
            else:
                index = index + 1

        return ret

    def isPowerOfThree(self, n: int) -> bool:
        aliquotList = self.findAliquot(n)

        if n == 0:
            return False

        for i in range(len(aliquotList)):
            if aliquotList[i] != pow(3, i):
                return False

        return True