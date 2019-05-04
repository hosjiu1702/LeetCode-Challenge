class Solution:
    def getNum(self, num: int) -> List[int]:
        b = num % 10
        a = int((num - b) / 10)

        return [a, b]

    def addStrings(self, num1: str, num2: str) -> str:
        ret = []

        num1List = []
        num2List = []
        n1 = len(num1)
        n2 = len(num2)

        for i in range(n1):
            num1List.append(num1[i])
        for j in range(n2):
            num2List.append(num2[j])

        if n1 <= n2:
            for i in range(n2-n1):
                num1List.insert(0, '0')
            n = n2
        else:
            for i in range(n1-n2):
                num2List.insert(0, '0')
            n = n1

        mem = 0
        for i in range(1, n+1):
            s = int(num1List[n-i]) + int(num2List[n-i]) + mem
            [mem, b] = self.getNum(s)
            ret.insert(0, str(b))
        if mem != 0:
            ret.insert(0, str(mem))

        return ''.join(ret)