class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--.."
        }

        for i in range(len(words)):
            s = ""
            for j in range(len(words[i])):
                s += morse[words[i][j]]
            words[i] = s

        words.sort()

        index = 0
        while index < len(words) - 1:
            if words[index] == words[index + 1]:
                words.pop(index)
            else:
                index = index + 1

        return len(words)