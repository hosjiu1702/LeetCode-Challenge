class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        startIndex = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(0, n - 1):
            for j in range(m - 2, -1, -1):
                startIndex.append([j, i])
        for k in range(len(startIndex)):
            i = startIndex[k][0]
            j = startIndex[k][1]
            x = 1
            while i + x < m and j + x < n:
                if matrix[i][j] != matrix[i + x][j + x]:
                    return False
                else:
                    x = x + 1

        return True