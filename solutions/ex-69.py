class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        # Find Degree
        t = nums.copy()
        t.sort()
        numsList = []
        
        n = len(t)
        degree = 1
        index = 0
        while index < n - 1:
            count = 1
            if t[index] != t[index + 1]:
                if count == degree:
                    numsList.append(t[index])
                index = index + 1
            else:
                while t[index] == t[index + 1]:
                    count = count + 1
                    index = index + 1
                    if index == n - 1:
                        break
                if count == degree:
                    numsList.append(t[index])
                elif count > degree:
                    numsList[:] = []
                    numsList.append(t[index])
                    degree = count
                index = index + 1

        indicesList = []
        for num in numsList:
            indicesList.append([])
            l = len(indicesList) - 1

            for i in range(n):
                if nums[i] == num:
                    indicesList[l].append(i)

        d = [x[-1] - x[0] + 1 for x in indicesList]

        return min(d)