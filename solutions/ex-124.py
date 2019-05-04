class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num+1):
            k = i * i
            if k > num:
                return False
            elif k == num:
                return True