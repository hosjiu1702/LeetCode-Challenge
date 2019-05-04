class Solution:
    def longestPalindrome(self, s: str) -> int:
        t = list()
        l = list()
        
        t = [letter for letter in s]
        
        t.sort()

        index = 0
        n = len(t)
        while index < n - 1:
            if t[index] != t[index + 1]:
                index = index + 1
            else:
                count = 1
                while t[index] == t[index + 1]:
                    count = count + 1
                    index = index + 1
                    if index == n - 1:
                        break
                m = ""
                for _ in range(count):
                    m += t[index]
                l.append(m)
                index = index + 1

        k = [len(i) - 1 if len(i) % 2 != 0 else len(i) for i in l]

        ret = sum(k)

        if sum([len(i) for i in l]) < n:
            return ret + 1

        for i in l:
            if len(i) % 2 != 0:
                return ret + 1

        return ret