from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_1 = 0
        index_2 = len(numbers) - 1
        while index_1 < index_2:
            s = numbers[index_1] + numbers[index_2]
            if s == target:
                return [index_1 + 1, index_2 + 1]
            if s < target:
                index_1 += 1
            else:
                index_2 -= 1


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))  # [1,2]
    print(Solution().twoSum([1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9))  # [1,2]
