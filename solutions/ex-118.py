class Solution:
    def generate(self, numRows: int):
        # ret[i+1][j] = ret[i][j-1] + ret[i][j]
        ret = [[None] * n for n in range(1, numRows+1)]

        for i in range(numRows):
            for j in range(i+1):
                if j == 0 or j == i:
                    ret[i][j] = 1
                else:
                    ret[i][j] = ret[i-1][j-1] + ret[i-1][j]
                    
        return ret

def main():
    solver = Solution()
    print(solver.generate(2))

if __name__ == "__main__":
    main()