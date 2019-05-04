class Solution:
    def dec2bin(self, num: int) -> List[int]:
        ret = []
        i = 0
        while num != 0:
            r = num % 2
            q = int((num - r) / 2)
            ret.insert(0, r)
            num = q
        return ret

    def countPrimeSetBits(self, L: int, R: int) -> int:
        ret = 0
        smallPrimes = [2, 3, 5, 7, 11, 13, 17, 19]
        
        binaryRoot = None
        for num in range(L, R + 1):
            if num == L:
                binaryRoot = bin(num)
                num1Bits = binaryRoot.count('1')
                if smallPrimes.count(num1Bits) == 1:
                    ret = ret + 1
            else:
                binaryDigits = self.dec2bin(num)
                numOfSetBits = binaryDigits.count(1)
                if smallPrimes.count(numOfSetBits) == 1:
                    ret = ret + 1

        return ret