class Solution:
    def romanToInt(self, s: str) -> int:
        mapTable = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000}

        n = len(s)

        ret = 0
        index = 0
        while index < n:
            if s[index] == 'I':
                if index + 1 < n:
                    if s[index + 1] == 'V':
                        ret = ret + 4
                    elif s[index + 1] == 'X':
                        ret = ret + 9
                    else:
                        ret = ret + mapTable[s[index]] + mapTable[s[index + 1]]
                    index = index + 2
                else:
                    ret = ret + 1
                    index = index + 1
                    break

            elif s[index] == 'X':
                if index + 1 < n:
                    if s[index + 1] == 'L' or s[index + 1] == 'C':
                        ret += mapTable[s[index + 1]] - mapTable[s[index]]
                        index = index + 2
                    elif s[index + 1] != 'I':
                        ret += mapTable[s[index]] + mapTable[s[index + 1]]
                        index = index + 2
                    else:
                        if index + 1 == n - 1:
                            ret += mapTable[s[index]] + mapTable[s[index + 1]]
                            break
                        else:
                            if s[index + 2] == 'V' or s[index + 2] == 'X':
                                ret += mapTable[s[index]]
                                index = index + 1
                            else:
                                ret += mapTable[s[index]] + mapTable[s[index + 1]]
                                index = index + 2
                else:
                    ret = ret + mapTable[s[index]]
                    break

            elif s[index] == 'C':
                if index + 1 < n:
                    if s[index + 1] == 'D' or s[index + 1] == 'M':
                        ret += mapTable[s[index + 1]] - mapTable[s[index]]
                        index = index + 2
                    elif s[index + 1] != 'X' and s[index + 1] != 'I':
                        ret = ret + mapTable[s[index]] + mapTable[s[index + 1]]
                        index = index + 2 
                    else:
                        if index + 1 == n - 1:
                            ret += mapTable[s[index]] + mapTable[s[index + 1]]
                            break
                        else:
                            if s[index + 1] == 'I':
                                if s[index + 2] == 'V' or s[index + 2] == 'X':
                                    ret += mapTable[s[index]]
                                    index = index + 1
                                else:
                                    ret += mapTable[s[index]] + mapTable[s[index + 1]]
                                    index = index + 2
                            elif s[index + 1] == 'X':
                                if s[index + 2] == 'L' or s[index + 2] == 'C':
                                    ret += mapTable[s[index]]
                                    index = index + 1
                                else:
                                    ret += mapTable[s[index]] + mapTable[s[index + 1]]
                                    index = index + 2                                
                else:
                    ret += mapTable[s[index]]
                    break

            else:
                ret += mapTable[s[index]]
                index = index + 1

        return ret