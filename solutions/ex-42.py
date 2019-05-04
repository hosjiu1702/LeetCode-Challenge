class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1

        while i != j:
            if nums[i] != 0:
                i += 1
            else:
                t = nums.pop(i)
                nums.append(t)
                j -= 1
