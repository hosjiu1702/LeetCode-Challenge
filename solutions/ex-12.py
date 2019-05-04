class Solution:
    def str2list(self, S: str) -> List[List[str]]:
        """
        Example: 
            Input: "Leetcode contest"
            Output: [['L','e','e','t','c','o','d','e'], ['c','o','n','t','e','s','t']]
        """
        sList = []
        index = 0
        j = -1
        while index < len(S):
            if S[index] != ' ':
                j = j + 1
                sList.append([])
            while S[index] != ' ':
                sList[j].append(S[index])
                index = index + 1
                if index == len(S):
                    break
            index = index + 1

        return sList

    def reverseWords(self, s: str) -> str:
        # Convert the sentence from str to List[str]
        sList = self.str2list(s)
        
        # Reverse order of every word in given sentence.
        for i in range(len(sList)):
            word = sList[i]
            n = len(word)
            m = math.floor(n / 2)

            # Reverse the current word
            for j in range(m):
                temp = word[j]
                word[j] = word[n - 1 - j]
                word[n - 1 - j] = temp

            # Convert current word from List[str] -> str
            sList[i] = ''.join(word)

        s = ' '.join(sList)

        return s