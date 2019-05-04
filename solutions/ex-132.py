class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n < 2:
            return [nums[0]]
        
        nums = [[nums[i], i] for i in range(n)]
        nums.sort(key=lambda x: x[0])
        
        i = 0
        j = n - 1
        
        s = nums[i][0] + nums[j][0]
        while s != target:
            if s < target:
                i = i + 1
            elif s > target:
                j = j - 1
                
            s = nums[i][0] + nums[j][0]
        
        return [nums[i][1], nums[j][1]]