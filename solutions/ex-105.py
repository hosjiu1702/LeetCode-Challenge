class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        sList = []
        extraList = []

        for i in range(len(S)):
            if S[i] != '-':
                sList.append(S[i].upper())
        n = len(sList)

        if n <= K:
            return ''.join(sList)

        r = n % K
        q = int((n - r) / K)

        if r != 0:
            for i in range(r):
                extraList.append(sList.pop(0))
            extraList.append('-')

        mainList = []
        for i in range(q):
            for j in range(K):
                mainList.append(sList.pop(0))
            if i < q-1:
                mainList.append('-')

        mainList[:0] = extraList
        return ''.join(mainList)