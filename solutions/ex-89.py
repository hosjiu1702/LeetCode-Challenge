class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        newNums = []
        n = len(nums)
        for i in range(n):
            newNums.append([nums[i], i])
        newNums.sort(key=lambda element: element[0])
        maxValue = (newNums[-1])[0]
        for i in range(0, n-1):
            if maxValue < 2*(newNums[i])[0]:
                return -1

        return (newNums[-1])[1]