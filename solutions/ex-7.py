class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        index = 0
        while index < len(nums):
        	s += nums[index]
        	index = index + 2

        return s