class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ret = 0
        for i in range(len(A[0])):
            for j in range(0, len(A) - 1):
                if A[j][i] > A[j+1][i]:
                    ret = ret + 1
                    break

        return ret