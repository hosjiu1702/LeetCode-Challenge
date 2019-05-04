import math

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
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x >= 0 and x <= 9:
            return True
        else:
            digitsList = self.getDigits(x)
            n = len(digitsList)
            for i in range(math.floor(n / 2)):
                if digitsList[i] != digitsList[n - i - 1]:
                    return False

            return True