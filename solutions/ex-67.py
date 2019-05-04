class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        
        arrS = []
        arrT = []
        
        for i in range(n1):
            arrS.append(s[i])
        for j in range(n2):
            arrT.append(t[j])
        
        arrS.sort()
        arrT.sort()
            
        if len(arrS) != len(arrT):
            return False
        
        for i in range(len(arrS)):
            if arrS[i] != arrT[i]:
                return False
        
        return True