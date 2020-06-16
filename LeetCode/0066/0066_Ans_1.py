from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(-1, -len(digits) - 1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    print(Solution().plusOne([1, 2, 3]))  # [1,2,4]
    print(Solution().plusOne([4, 3, 2, 1]))  # [4,3,2,2]
    print(Solution().plusOne([9]))  # [1,0]
