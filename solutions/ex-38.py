class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        CASE1 = True
        CASE2 = True
        CASE3 = True

        n = len(word)

        for i in range(n):
            if word[i].islower():
                CASE1 = False
                break
        if CASE1:
            return True

        for i in range(n):
            if word[i].isupper():
                CASE2 = False
                break
        if CASE2:
            return True

        for i in range(n):
            if i == 0:
                if word[i].islower():
                    CASE3 = False
            else:
                if word[i].isupper():
                    CASE3 = False
        if CASE3:
            return True

        return False