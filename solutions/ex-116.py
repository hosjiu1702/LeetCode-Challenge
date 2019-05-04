class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret1 = None
        ret2 = None

        nums.sort()

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                ret1 = nums[i]
                nums.pop(i)
                break

        sumNums = sum(nums)
        refVal = int((n * (n + 1)) / 2)
        for val in range(1, n+1):
            if refVal == val + sumNums:
                ret2 = val
                break

        return [ret1, ret2]