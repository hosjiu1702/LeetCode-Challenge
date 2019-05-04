class Solution:
    def maxCount(self, m, n, ops):
        min_x = m
        min_y = n
        for op in ops:
            if min_x > op[0]:
                min_x = op[0]
            
            if min_y > op[1]:
                min_y = op[1]
        
        return min_x * min_y
        
    """
        # Init number of rows and cols of the matrix M
        row_mat = m
        col_mat = n

        # Init zeros value to all of values of matrix M
        M = []
        for r in range(row_mat):
            # Increment +1 row to M
            M.append([])
            for c in range(col_mat):
                M[r].append(0)

        # Apply ops step by step to matrix M
        for op in ops:
            for r in range(op[0]):
                for c in range(op[1]):
                    M[r][c] += 1

        M = self.flaten(m, n, M)
        M.sort()
        # self.sortListAscend(M)
        
        max_M = M[-1]
        max_count = M.count(max_M)
        
        return max_count
    """

    """
    def flaten(self, m, n, arr):
        arr_ = []        
        for row in range(m):
            for col in range(n):
                arr_.append(arr[row][col])
        return arr_

    def sortListAscend(self, arr):
        # Lenght of 'arr' list
        n = len(arr)

        index = 0
        # Loop (n-1) times to compare
        for j in range(n-1):
            num_iters = n - 1 - index
            for k in range(num_iters):
                if arr[index] > arr[(index+1) + k]:
                    # Swap
                    temp = arr[index]
                    arr[index] = arr[(index+1) + k]
                    arr[(index+1) + k] = temp
            index = index + 1
    """

def main():
    solver = Solution()
    print(solver.maxCount(3000, 3000, [[2000, 2000], [3000, 3000]]))

if __name__ == "__main__":
    main()