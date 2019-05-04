class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # sum - minNum * n = m
        n = len(nums)
        
        sum = 0
        for i in range(n):
            sum += nums[i]
        
        nums.sort()
        minNum = nums[0]
        
        m = sum - minNum * n
        return m