class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        n1 = len(list1)
        n2 = len(list2)
        
        temp = []
        
        for i in range(n1):
            for j in range(n2):
                if list1[i] == list2[j]:
                    temp.append([list1[i], i+j])
        
        temp.sort(key=lambda restaurant: restaurant[1])
        
        MIN_INDEX_SUM = (temp[0])[1]
        m = len(temp)
        ret = []
        
        index = 0
        for i in range(m):
            if (temp[i])[1] == MIN_INDEX_SUM:
                ret.append((temp[i])[0])
            else:
                break

        return ret