class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)

        i = 0
        while i < n - 1:
            if bits[i]:
                bits[i] = None
                bits[i+1] = None
                i += 2
            else:
                i += 1

        if bits[-1] != None:
            return True

        return False