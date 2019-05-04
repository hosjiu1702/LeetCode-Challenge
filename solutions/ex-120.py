class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            False

        uglyFactor = [2, 3, 5]
        for i in range(len(uglyFactor)):
            flag = True
            while flag:
                r = n % uglyFactor[i]
                q = int((n - r) / uglyFactor[i])
                if r == 0:
                    n = q
                    if q == 0:
                        flag = False
                else:
                    flag = False

        print(n)
        if n == 1:
            return True

        return False