class Solution:
    def validate(self, x: int, y: int, m: int, n: int) -> bool:
        if x >= 0 and x < m:
            if y >= 0 and y < n:
                return True
        return False

    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        """
        [[(i-1, j-1)], [(i-1, j)], [(i-1, j+1)],
         [(i  , j-1)], [(i  , j)], [(i  , j+1)],
         [(i+1, j-1)], [(i+1, j)], [(i+1, j+1)]]
        """
        # M: mxn matrix
        m = len(M)
        n = len(M[0])

        ret = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                a = [0 for _ in range(9)]
                index = 0
                count = 0
                for p in range(-1, 2):
                    for q in range(-1, 2):
                        x = i + p
                        y = j + q
                        if self.validate(x, y, m, n):
                            a[index] = M[x][y]
                            index = index + 1
                        else:
                            count = count + 1
                            index = index + 1
                denominator = len(a) - count
                ret[i][j] = math.floor(sum(a) / denominator)

        return ret