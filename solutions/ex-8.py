class Solution:
    def isVowel(self, c: str) -> bool:
        if c.lower() == 'u':
            return True
        elif c.lower() == 'e':
            return True
        elif c.lower() == 'o':
            return True
        elif c.lower() == 'a':
            return True
        elif c.lower() == 'i':
            return True
        return False

    def toGoatLatin(self, S: str) -> str:
        # Convert string to list of words
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
        
        # Loop over each word in the sentence
        # Convert the current word -> Goat Latin
        for i in range(len(sList)):
            word = sList[i]
            
            # if word starts with a vowel
            if self.isVowel(word[0]):
                word.append("ma")
            # if word starts with a consonant
            else:
                c = word.pop(0)
                word.append(c)
                word.append("ma")

            # Add 'a'
            for j in range(i + 1):
                word.append('a')

        # Convert from list to string
        for i in range(len(sList)):
            sList[i] = ''.join(sList[i])

        s = ' '.join(sList)

        return s