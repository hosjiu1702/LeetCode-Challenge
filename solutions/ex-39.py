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

    def addDigits(self, num: int) -> int:
        while num > 9:
        	digits = self.getDigits(num)
        	num = sum(digits)

        return num