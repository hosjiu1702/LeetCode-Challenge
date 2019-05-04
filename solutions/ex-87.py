"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string.
If there are less than k characters left, reverse all of them. 
If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:
    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"

Restrictions:
    - The string consists of lower English letters only.
    - Length of the given string and k will in the range [1, 10000]
"""
class Solution:
    def reverse(self, arr, m: int):
        n = len(arr)
        ret = []
        for i in range(m-1, -1, -1):
            ret.append(arr[i])

        for i in range(m, n):
            ret.append(arr[i])
        
        return ret
    def delSubArr(self, arr, m: int):
        for i in range(m):
            arr.pop(0)

    def reverseStr(self, s: str, k: int) -> str:
        ret = []
        n = len(s)

        sList = []
        for i in range(n):
            sList.append(s[i])
        
        while len(sList) != 0:
            l = len(sList)
            if l >= 2*k:
                tempStr = self.reverse(sList[:2*k], k)
                ret.extend(tempStr)
                self.delSubArr(sList, 2*k)
            elif l >= k and l < 2*k:
                tempStr = self.reverse(sList[:l], k)
                ret.extend(tempStr)
                self.delSubArr(sList, l)
            else:
                tempStr = self.reverse(sList, l)
                ret.extend(tempStr)
                self.delSubArr(sList, l)
        
        s = ''.join(ret)
        return s
"""
def main():
    s = "abcd"
    randList = ['a', 'b', 'c', 'c']
    k = 4

    solver = Solution()
    ret = solver.reverse(s, k)

    print("s = {}".format(s))
    print("reversed s = {}".format(ret))

    solver.delSubArr(randList, 3)
    print(randList)

if __name__ == "__main__":
    main()
"""