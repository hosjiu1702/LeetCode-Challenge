class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(A[0])

        ret = [[None] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i != j:
                    ret[i][j] = A[j][i]
                else:
                    ret[i][j] = A[i][j]

        return ret