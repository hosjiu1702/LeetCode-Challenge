class Solution:
    def findAliquot(self, n: int) -> List[int]:
        ret = []

        if n < 2:
            return [1]

        for b in range(1, n):
            r = n % b
            if r == 0:
                q = int((n - r) / b)
                ret.append(b)
                ret.append(q)
        ret.sort()

        index = 0
        while index < len(ret) - 1:
            if ret[index] == ret[index+1]:
                ret.pop(index)
            else:
                index = index + 1

        return ret

    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        t = self.findAliquot(n)
        for i in range(len(t)):
            if s[:t[i]] == s[t[i]:2*t[i]]:
                k = t[i]
                numIter = int(n/k) - 1
                retFlag = True
                for j in range(numIter):
                    if s[k*j:k*(j+1)] != s[k*(j+1):k*(j+2)]:
                        retFlag = False
                        break
                if retFlag:
                    return True

        return False