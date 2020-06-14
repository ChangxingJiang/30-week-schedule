from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            another = target - nums[i]
            if another in nums[(i + 1):]:
                return [i, nums[(i + 1):].index(another) + i + 1]


if __name__ == "__main__":
    print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))  # [0,1]
    print(Solution().twoSum(nums=[3, 2, 4], target=6))  # [1,2]
    print(Solution().twoSum(nums=[3, 3], target=6))  # [0,1]
