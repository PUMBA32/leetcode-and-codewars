# 329

class Solution:
    @staticmethod
    def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        min_arr = nums1 if len(nums1) < len(nums2) else nums2
        for el in min_arr:
            if el not in result and el in nums1 and el in nums2:
                result.append(el)
        return result


print(Solution.intersection([1,2,2,1], [2,2]))  # [2]
print(Solution.intersection([4,9,5], [9,4,9,8,4]))  # [9,4]
        