"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, 
who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:

Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

Explanation: The first three athletes got the top three highest scores, so they got 
"Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.

Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
"""

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        INDEX = 1
        SCORE = 0
        RANK = 0
        n = len(nums)

        # Create [[a_0, i_0] ... [a_n, i_n]] data structure
        newNums = []
        for i in range(n):
            newNums.append([nums[i], i])
        newNums.sort(key=lambda athletes: athletes[SCORE])
        
        for i in range(len(newNums)):
            if i < n-3:
                (newNums[i])[RANK] = str(n - i)
            else:
                # Gold medal
                if i == n-3:
                    (newNums[i])[RANK] = "Bronze Medal"
                # Silver Medal
                elif i == n-2:
                    (newNums[i])[RANK] = "Silver Medal"
                # Bronze Medal
                else:
                    (newNums[i])[RANK] = "Gold Medal"

        newNums.sort(key=lambda athletes: athletes[INDEX])

        leaderBoard = []
        for i in range(n):
            leaderBoard.append((newNums[i])[RANK])
        
        return leaderBoard