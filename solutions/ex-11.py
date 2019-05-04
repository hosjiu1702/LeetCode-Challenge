import math

class Solution:
    def invert(self, pixel: int) -> int:
        if pixel == 0:
            return 1
        return 0

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        m = math.floor(n / 2)
        
        for i in range(n):
            for j in range(m):
                # Flip row
                temp = A[i][j]
                A[i][j] = A[i][n - 1 - j]
                A[i][n - 1 - j] = temp

                # Invert
                A[i][j] = self.invert(A[i][j])
                A[i][n - 1 - j] = self.invert(A[i][n - 1 - j])

        # Invert (cont)
        if n % 2 != 0:
            for i in range(n):
                A[i][m] = self.invert(A[i][m])

        return A