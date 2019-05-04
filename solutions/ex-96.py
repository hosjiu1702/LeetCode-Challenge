class Solution:
    def getNum(self, num:int):
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

    def isHappy(self, n: int) -> bool:
        count = 0
        while True:
            numsList = self.getNum(n)
            sumOfSquare = 0
            for i in range(len(numsList)):
                sumOfSquare += pow(numsList[i], 2)
            if sumOfSquare < 10:
                if sumOfSquare == 1:
                    return True
                else:
                    if count > 10:
                        return False
            n = sumOfSquare
            count = count + 1

def main():
    solver = Solution()

    x1 = 121
    x2 = 11
    x3 = 2
    
    print("x1 = {}".format(solver.getNum(x1)))
    print("x2 = {}".format(solver.getNum(x2)))
    print("x3 = {}".format(solver.getNum(x3)))

if __name__ == "__main__":
    main()