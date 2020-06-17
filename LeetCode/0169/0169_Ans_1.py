from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = len(nums) / 2
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        for num, count in hashmap.items():
            if count > s:
                return num


if __name__ == "__main__":
    print(Solution().majorityElement([3, 2, 3]))  # 3
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
