from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] != nums[i]:
                m += 1
                nums[m] = nums[i + 1]
        return m + 1


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums), nums)  # [1,2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(nums), nums)  # [0,1,2,3,4]
    nums = [-1, 0, 0, 0, 0, 3, 3]
    print(Solution().removeDuplicates(nums), nums)  # [-1,0,3]
