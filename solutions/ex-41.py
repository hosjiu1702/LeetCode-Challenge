class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = list()

        nums.sort()

        i = 0
        j = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                j += 1
            else:
                while nums[i] == nums[j]:
                    j += 1
                    if j == len(nums):
                        break
                for _ in range(j - i - 1):
                    nums.pop(i)
                j = i + 1

        t = [None] * n

        for num in nums:
            index = num - 1
            t[index] = num

        for i in range(n):
            if t[i] == None:
                ret.append(i + 1)

        return ret