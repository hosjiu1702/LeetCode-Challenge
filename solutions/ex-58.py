class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if n % 2 == 0:
            return nums[int(n / 2)]
        else:
            return nums[int((n-1) / 2)]
        
        """
        for i in range(n):
            if nums.count(nums[i]) > n/2:
                return nums[i]
        """