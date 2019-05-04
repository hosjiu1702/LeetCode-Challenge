class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        nums.sort()
        index = 0
        while index < n:
            if index < n - 1:
                if nums[index] != nums[index + 1]:
                    return nums[index]
                else:
                    index = index + 2
            else:
                return nums[index]