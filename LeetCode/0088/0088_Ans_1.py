from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index_1 = m - 1
        index_2 = n - 1
        for i in range(m + n - 1, -1, -1):
            if index_1 < 0 or (index_2 >= 0 and nums2[index_2] > nums1[index_1]):
                nums1[i] = nums2[index_2]
                index_2 -= 1
            else:
                nums1[i] = nums1[index_1]
                index_1 -= 1


if __name__ == "__main__":
    list_1 = [1, 2, 3, 0, 0, 0]
    list_2 = [2, 5, 6]
    print(Solution().merge(list_1, 3, list_2, 3), list_1)
