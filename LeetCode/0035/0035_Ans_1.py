from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        len_num = len(nums)
        for i in range(len_num):
            if nums[i] >= target:
                return i
        return len_num


if __name__ == "__main__":
    print(Solution().searchInsert([1, 3, 5, 6], 5))  # 2
    print(Solution().searchInsert([1, 3, 5, 6], 2))  # 1
    print(Solution().searchInsert([1, 3, 5, 6], 7))  # 4
    print(Solution().searchInsert([1, 3, 5, 6], 0))  # 0
