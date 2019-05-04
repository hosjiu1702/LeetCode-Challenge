class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n1 = len(nums1)
        n2 = len(nums2)
        ret = []

        for i in range(n1):
        	while nums2 != []:
        		if nums1[i] == nums2[0]:
        			ret.append(nums1[i])
        			nums2.pop(0)
        			break
        		elif nums1[i] > nums2[0]:
        			nums2.pop(0)
        		else:
        			break

        return ret