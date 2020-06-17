from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(numbers)):
            n = numbers[i]
            a = target - n
            if a in hashmap:
                return [hashmap[a], i + 1]
            hashmap[n] = i + 1


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))  # [1,2]
