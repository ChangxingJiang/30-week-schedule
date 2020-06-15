from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        m = 0
        for i in range(len(nums)):
            d = nums[i]
            if d != val:
                nums[m] = nums[i]
                m += 1
        return m


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    print(Solution().removeElement(nums, 3), nums)
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    print(Solution().removeElement(nums, 2), nums)
