class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        # Sort candies by type
        candies.sort()
        types = []
        i = 0
        while i < len(candies):
            types.append([])
            currentType = len(types) - 1
            if i < len(candies) - 1:
                if candies[i] != candies[i + 1]:
                    types[currentType].append(candies[i])
                    i = i + 1
                else:
                    while candies[i] == candies[i + 1]:
                        types[currentType].append(candies[i])
                        i = i + 1
                        if i == len(candies) - 1:
                            break
                    types[currentType].append(candies[i])
                    i = i + 1
            else:
                types[currentType].append(candies[i])
                i = i + 1

        # Take a candy from each different types[i]
        # until number of candies of sister == len(candies) / 2
        if len(types) < int(len(candies) / 2):
            return len(types)

        return int(len(candies) / 2)