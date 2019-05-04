class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # maxSum = nums[0]
        temp = []
        currSum = sum([nums[i] for i in range(0, k)])
        temp.append(currSum)
        for i in range(1, len(nums)):
            if i + k - 1 >= len(nums):
                break
            currSum = (currSum - nums[i-1] + nums[k-1+i])
            temp.append(currSum)
        
        temp.sort()
        maxAverage = temp[-1] / k
        
        return maxAverage