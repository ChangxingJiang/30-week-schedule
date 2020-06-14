from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index


if __name__ == "__main__":
    print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))  # [0,1]
    print(Solution().twoSum(nums=[3, 2, 4], target=6))  # [1,2]
    print(Solution().twoSum(nums=[3, 3], target=6))  # [0,1]
