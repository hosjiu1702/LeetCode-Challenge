class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sumL = 0
        sumR = sum(nums)

        for i in range(n):
            if i-1 >= 0:
                sumL = sumL + nums[i-1]
            sumR = sumR - nums[i]

            if sumL == sumR:
                return i

        return -1