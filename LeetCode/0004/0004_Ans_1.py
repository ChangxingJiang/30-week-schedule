from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        count = len(nums)
        if count % 2 == 0:
            return (nums[int(count / 2 - 1)] + nums[int(count / 2)]) / 2
        else:
            return nums[int(count / 2)]


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 3], [2]))
    print(Solution().findMedianSortedArrays([1, 3], [2, 4]))
