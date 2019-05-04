"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""
class Solution:
    def countSegments(self, s: str) -> int:
        n = len(s)
        
        indexOfSpace = []
        for i in range(n):
            if ord(s[i]) == 32:
                indexOfSpace.append(i)
        if len(indexOfSpace) == n:
            return 0
        elif len(indexOfSpace) == 0:
            return 1

        i = 0
        while i < len(indexOfSpace) - 1:
            if indexOfSpace[i] == indexOfSpace[i+1] - 1:
                indexOfSpace.pop(i)
            else:
                i = i + 1

        k = len(indexOfSpace)

        if ord(s[0]) == 32 and ord(s[-1]) == 32:
            return k - 1
        elif ord(s[0]) == 32 or ord(s[-1]) == 32:
            return k
        else:
            return k + 1