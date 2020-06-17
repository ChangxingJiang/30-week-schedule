from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = set()
        for n in nums:
            if n not in hashset:
                hashset.add(n)
            else:
                hashset.remove(n)
        return hashset.pop()


if __name__ == "__main__":
    print(Solution().singleNumber([2, 2, 1]))  # 1
    print(Solution().singleNumber([4, 1, 2, 1, 2]))  # 4
