class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []

        for num in nums1:
            k = None
            for i in range(len(nums2)):
                if nums2[i] == num:
                    k = i
                    break
            if k != len(nums2) - 1:
                for i in range(k + 1, len(nums2)):
                    if nums2[i] > num:
                        ret.append(nums2[i])
                        break
                    else:
                        if i == len(nums2) - 1:
                            ret.append(-1)
            else:
                ret.append(-1)

        return ret