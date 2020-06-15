from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        now = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            if maximum < 0 and n > maximum:
                maximum = n
                now = n
            else:
                now += n
                if now < n:
                    now = n
                if now > maximum:
                    maximum = now
        return maximum


if __name__ == "__main__":
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
