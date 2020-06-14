from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_1 = len(nums1)
        len_2 = len(nums2)
        total = len_1 + len_2

        left = -1
        right = -1

        index_1 = 0
        index_2 = 0

        for i in range(int(total / 2) + 1):
            left = right
            if index_1 < len_1 and (index_2 >= len_2 or nums1[index_1] < nums2[index_2]):
                right = nums1[index_1]
                index_1 += 1
            else:
                right = nums2[index_2]
                index_2 += 1

        if total % 2 == 0:
            return (left + right) / 2
        else:
            return right


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 3], [2]))  # 2
    print(Solution().findMedianSortedArrays([1, 3], [2, 4]))  # 2.5
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))  # 2.5
