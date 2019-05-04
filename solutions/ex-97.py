"""
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
    Input: [1,3,2,2,5,2,3,7]
    Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
"""
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
    
        longestLen = 0
        for i in range(n):
            baseIndex = i
            index = baseIndex + 1
            refVal = nums[baseIndex]
            currLen = 1

            while index < n:
                currVal = nums[index]
                if currVal == refVal or currVal == refVal + 1:
                    currLen = currLen + 1
                    index = index + 1
                else:
                    break
            if nums[baseIndex] != nums[index-1]:
                if currLen >= longestLen:
                    longestLen = currLen

        return longestLen