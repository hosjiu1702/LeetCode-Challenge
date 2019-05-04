class Solution:
    def climbStairs(self, n: int) -> int:
        # Fibonacci sequence
        fn_1 = 2
        fn_2 = 1

        if n == 1:
            return fn_2
        
        elif n == 2:
            return fn_1
        
        else:
            i = 2
            while i < n:               
                f = fn_1 + fn_2
                fn_2 = fn_1
                fn_1 = f
                
                i += 1

        return f