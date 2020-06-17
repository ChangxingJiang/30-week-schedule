from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = 0
        for n in nums:
            s = s ^ n
        return s


if __name__ == "__main__":
    print(Solution().singleNumber([2, 2, 1]))  # 1
    print(Solution().singleNumber([4, 1, 2, 1, 2]))  # 4
