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

    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            x = abs(x)
            isNegative = True
        
        digitsList = self.getDigits(x)
        digitsList.reverse()

        ret = 0
        n = len(digitsList)
        for i in range(n):
            ret += digitsList[n-1-i] * pow(10, i)
        if isNegative:
            ret = -ret

        if ret <= pow(2, 31) - 1 and ret >= pow(-2, 31):
            return ret

        return 0