class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = [[None] * n for n in range(1, rowIndex+2)]

        for i in range(rowIndex+1):
            for j in range(i+1):
                if j == 0 or j == i:
                    ret[i][j] = 1
                else:
                    ret[i][j] = ret[i-1][j-1] + ret[i-1][j]
        
        return ret[-1]