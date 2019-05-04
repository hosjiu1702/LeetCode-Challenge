class Solution:
    def titleToNumber(self, s: str) -> int:
        # length of s
        n = len(s)
        
        sum = 0
        for i in range(n):
            sum += self.location(s[i]) * pow(26, n-1-i)

        return sum
    
    # Define location function of a character
    def location(self, x: str):
        for i in range(26):
            if x == chr(i+65):
                return i+1