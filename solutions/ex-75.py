import math

class Solution:
    def squareDistance(self, p1: List[int], p2: List[int]) -> int:
        return (pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ret = 0

        m = len(points)
        for centerPoint in points:
            for l in range(0, m):
                if points[l] != centerPoint:
                    for r in range(l+1, m):
                        if points[r] != centerPoint and points[r] != points[l]:
                            if self.squareDistance(centerPoint, points[l]) == self.squareDistance(centerPoint, points[r]):
                                ret = ret + 2

        return ret