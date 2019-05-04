class Solution:
    def decToBin(self, num: int) -> List[int]:
        ret = []

        i = 0
        while num != 0:
            r = num % 2
            q = int((num - r) / 2)
            ret.insert(0, r)
            num = q

        return ret

    def hammingDistance(self, x: int, y: int) -> int:
        # Convert x, y to base-2 and store its digits to 2 separate arrays.
        xBinaryDigits = self.decToBin(x)
        yBinaryDigits = self.decToBin(y)
        
        # Align digits list (if any) to traverse
        if len(xBinaryDigits) < len(yBinaryDigits):
            k = len(yBinaryDigits) - len(xBinaryDigits)
            for i in range(k):
                xBinaryDigits.insert(0, 0)
        else:
            k = len(xBinaryDigits) - len(yBinaryDigits)
            for i in range(k):
                yBinaryDigits.insert(0, 0)

        hammingDistance = 0
        for j in range(len(xBinaryDigits)):
            if xBinaryDigits[j] != yBinaryDigits[j]:
                hammingDistance = hammingDistance + 1

        return hammingDistance