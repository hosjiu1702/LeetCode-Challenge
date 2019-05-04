class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binaryDigits = []
        while n != 0:
            r = n % 2
            q = int((n - r) / 2)
            binaryDigits.append(r)
            n = q
            
        count = binaryDigits.count(1)

        return count