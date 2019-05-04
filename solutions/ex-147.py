class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sList = []
        for i in range(len(s)):
            sList.append([s[i], i])

        sList.sort(key=lambda x: x[0])

        indexList = []
        index = 0
        count = 1
        j = -1
        while index < len(sList) - 1:
            if sList[index][0] != sList[index + 1][0]:
                index = index + 1
            else:
                while sList[index][0] == sList[index + 1][0]:
                    count = count + 1
                    index = index + 1
                    if index == len(sList) - 1:
                        break
                j = j + 1
                indexList.append([])
                for i in range(count):
                    indexList[j].append(sList[index - i][1])
                count = 1
                index = index + 1

        if len(indexList) == 0:
            tList = []
            for i in range(len(t)):
                tList.append(t[i])
            tList.sort()
            index = 0
            while index < len(tList) - 1:
                if tList[index] == tList[index + 1]:
                    return False
                index = index + 1
        else:
            for m in range(len(indexList)):
                k = []
                for n in range(len(indexList[m])):
                    k.append(t[indexList[m][n]])
                if k.count(k[0]) != len(k) or t.count(k[0]) != len(k):
                    return False

        return True