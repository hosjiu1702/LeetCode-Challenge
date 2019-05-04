class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
    	if n < 0:
    		return False

    	while n > 0:
    		r = n % 2
    		q = int((n - r) / 2)
    		if r == 0:
    			r2 = q % 2
    			if r2 != 0 and r2 != 1:
    				return False
    		else:
    			if q == 0:
    				return True
    			return False
    		n = q
    	
    	return False