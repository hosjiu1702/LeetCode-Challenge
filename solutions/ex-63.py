class Solution:
    def firstUniqChar(self, s: str) -> int:
        sList = []

        n = len(s)
        for i in range(n):
            sList.append([s[i], i])

        sList.sort(key=lambda x: x[0])

        index = 0
        while index < len(sList) - 1:
            if sList[index][0] != sList[index + 1][0]:
                index = index + 1
            else:
                base = index
                count = 1
                while sList[index][0] == sList[index + 1][0]:
                    count = count + 1
                    index = index + 1
                    if index == len(sList) - 1:
                        break
                for _ in range(count):
                    sList.pop(base)
                index = base
        
        sList.sort(key=lambda x: x[1])
        
        if len(sList) == 0:
            return -1

        return sList[0][1]