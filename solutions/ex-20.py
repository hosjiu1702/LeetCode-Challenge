class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(nums)
        n = len(nums[0])

        if r * c != m * n:
            return nums

        ret = [[None] * c for i in range(r)]

        temp = []
        for i in range(m):
            for j in range(n):
                temp.append(nums[i][j])

        for i in range(r):
            for j in range(c):
                ret[i][j] = temp.pop(0)

        return ret