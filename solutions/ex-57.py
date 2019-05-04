class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        num_str1 = len(ransomNote)
        num_str2 = len(magazine)
        
        arr1 = []
        arr2 = []
        
        for i in range(num_str1):
            arr1.append(ransomNote[i])
        
        for j in range(num_str2):
            arr2.append(magazine[j])
            
        count = 0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if arr1[i] == arr2[j]:
                    count = count + 1
                    arr2.remove(arr2[j])
                    break
                    
        if count == num_str1:
            return True
        
        return False
                