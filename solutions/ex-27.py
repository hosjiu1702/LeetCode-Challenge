class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) > len(b):
            return len(a)
        elif len(a) < len(b):
            return len(b)
        else:
            if a == b:
                return -1
            return len(a)