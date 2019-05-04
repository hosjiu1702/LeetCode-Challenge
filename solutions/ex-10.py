class Solution:
    def findComplement(self, num: int) -> int:
        binaryDigits = []

        # Convert num from base-10 to base-2
        while num != 0:
            r = num % 2
            q = int((num - r) / 2)
            num = q
            binaryDigits.insert(0, r)

        # Flip bits
        n = len(binaryDigits)
        for i in range(n):
            if binaryDigits[i] == 0:
                binaryDigits[i] = 1
            else:
                binaryDigits[i] = 0

        # Convert num (flipped bits) to base-10
        ret = 0
        for i in range(n):
            ret += binaryDigits[i] * pow(2, n - 1 - i)

        return ret