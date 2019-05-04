class Solution:
    def countAndSay(self, n: int) -> str:
        di = {1: ["1"]}
        
        for i in range(2, 31):
            temp = di[i-1]
            di[i] = []
            m = len(temp)
            count = 1
            if m < 2:
                di[i].append(str(count))
                di[i].append(temp[0])
            else:
                j = 0
                while j < m:
                    if j == m - 1:
                        di[i].append(str(count))
                        di[i].append(temp[j])
                    else:
                        if temp[j + 1] != temp[j]:
                            di[i].append(str(count))
                            di[i].append(temp[j])
                        else:
                            while temp[j + 1] == temp[j]:
                                count = count + 1
                                j = j + 1
                                if j == m - 1:
                                    break
                            di[i].append(str(count))
                            di[i].append(temp[j])
                            count = 1
                    j = j + 1

        return ''.join(di[n])