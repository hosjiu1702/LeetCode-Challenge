class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False

        power = 0
        while num > pow(4, power):
            power = power + 1

        if num == pow(4, power):
            return True

        return False