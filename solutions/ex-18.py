class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []

        i = 1
        while i <= n:
        	if i % 15 == 0:
        		ret.append("FizzBuzz")
        	elif i % 3 == 0:
        		ret.append("Fizz")
        	elif i % 5 == 0:
        		ret.append("Buzz")
        	else:
        		ret.append(str(i))
        	i = i + 1

        return ret