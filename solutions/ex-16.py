class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s = 0
        pointsData = []
        n = len(ops)
        for i in ops:
            if i == 'C':
                s -= pointsData.pop(-1)
            elif i == 'D':
                points = 2 * pointsData[-1]
                pointsData.append(points)
                s += points
            elif i == '+':
                points = pointsData[-1] + pointsData[-2]
                pointsData.append(points)
                s += points
            else:
                points = int(i)
                pointsData.append(points)
                s += points

        return s