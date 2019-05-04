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

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret = []

        for num in range(left, right + 1):
            # Get digits of the current number
            digits = self.getDigits(num)

            # Check zero digits
            isOut = False
            for i in range(len(digits)):
                if digits[i] == 0:
                    isOut = True
                    break

            if not isOut:
                isSelfDividingNumber = True
                for i in range(len(digits)):
                    if num % digits[i] != 0:
                        isSelfDividingNumber = False
                        break
                if isSelfDividingNumber:
                    ret.append(num)

        return ret