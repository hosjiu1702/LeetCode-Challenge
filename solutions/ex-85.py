class Solution:
    def convertToBase7(self, num: int) -> str:
        s = ""
        sign = ""
        
        if num == 0:
            return "0"
        
        if num < 0:
            sign = '-'
            num = -num
        
        while num != 0:
            r = num % 7
            q = int((num - r) / 7)
            
            s = str(r) + s
            num = q
        
        return sign + s