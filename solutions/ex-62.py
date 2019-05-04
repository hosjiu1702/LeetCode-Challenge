class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ret = 0
        g.sort()
        s.sort()
        for i in range(len(g)):
            count = 0
            for j in range(len(s)):
                if s[j] < g[i]:
                    count = count + 1
                else:
                    ret = ret + 1
                    count = count + 1
                    break
            if len(s) != 0:
                self.deleteRangeOfList(s, count)
            else:
                break
        return ret
    
    def deleteRangeOfList(self, arr: List[int], k: int):
        for i in range(k):
            arr.pop(0)