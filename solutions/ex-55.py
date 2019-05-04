class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []

        nums1.sort()
        nums2.sort()

        for k in range(2):
            if k == 0:
                num = nums1
            else:
                num = nums2

            n = len(num)

            if n >= 2:
                i = 0
                j = 1
                while j < len(num):
                    if num[i] != num[j]:
                        i += 1
                        j += 1
                    else:
                        num.pop(i)

        nums1_dict = {v: i for i, v in enumerate(nums1)}
        nums2_dict = {v: i for i, v in enumerate(nums2)}

        for num in nums1:
            if num in nums2_dict:
                ret.append(num)
                nums2_dict.pop(num)

        return ret