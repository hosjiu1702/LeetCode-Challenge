class Solution:
	def checkRecord(self, s: str) -> bool:
		sList = []
		n = len(s)
		
		for i in range(n):
			sList.append(s[i])
		
		# sList.sort()
		
		absentCount = 0
		latePrevious = False
		lateContinous = False
		for i in range(n):
			if sList[i] == 'A':
				absentCount = absentCount + 1
				if absentCount == 2:
					return False
				lateContinous = False
				latePrevious = False
			elif sList[i] == 'L':
				if lateContinous:
					return False
				else:
					if not latePrevious:
						latePrevious = True
						lateContinous = False
					else:
						lateContinous = True
			else:
				lateContinous = False
				latePrevious = False
		return True