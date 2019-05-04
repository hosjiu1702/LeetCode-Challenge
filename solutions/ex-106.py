class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        currIndex = 0
        while currIndex < len(nums):
            if nums[currIndex] == val:
                nums.pop(currIndex)
            else:
                currIndex = currIndex + 1

        return len(nums)