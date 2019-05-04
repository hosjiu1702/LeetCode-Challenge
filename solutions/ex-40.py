class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        ret = 0
        t = []

        index = 0
        while index < n:
            if index < n - 1:
                if s[index] != s[index + 1]:
                    t.append(s[index])
                    index = index + 1
                else:
                    base = index
                    while s[index] == s[index + 1]:
                        index = index + 1
                        if index == n - 1:
                            break
                    if index != n - 1:
                        t.append(s[base:index+1])
                        index = index + 1
                    else:
                        t.append(s[base:])
                        index = index + 1
            else:
                t.append(s[index])
                index = index + 1

        m = len(t)
        for i in range(t-1):
            l = len(t[i])
            r = len(t[i + 1])
            if l == r:
                ret = ret + l
            elif l < r:
                ret = ret + l
            else:
                ret = ret + r

        return ret