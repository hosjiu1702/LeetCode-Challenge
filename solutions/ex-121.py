class Solution:
    def getDigits(self, num:int) -> List[int]:
        ret = []
            
        i = 0
        while True:
            r = num % pow(10, i)
            if r != num:
                i = i + 1
            else:
                break

        for j in range(1, i+1):
            b = pow(10, i-j)
            r = num % b
            q = int((num - r) / b)
            ret.append(q)
            num = r

        return ret

    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        num = 0
        for i in range(n):
            num += digits[i] * pow(10, n-1-i)

        num = num + 1

        ret = self.getDigits(num)

        return ret