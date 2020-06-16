import math


class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        return int((pow((1 + sqrt5) / 2, n + 1) - pow((1 - sqrt5) / 2, n + 1)) / sqrt5)


if __name__ == "__main__":
    print(Solution().climbStairs(2))  # 2
    print(Solution().climbStairs(3))  # 3
    print(Solution().climbStairs(10))  # 89
    print(Solution().climbStairs(20))  # 89
