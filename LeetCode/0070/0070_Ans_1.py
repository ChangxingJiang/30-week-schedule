class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in range(3, n + 1):
                c = a + b
                a = b
                b = c
        return b


if __name__ == "__main__":
    print(Solution().climbStairs(2))  # 2
    print(Solution().climbStairs(3))  # 3
    print(Solution().climbStairs(10))  # 89
    print(Solution().climbStairs(20))  # 10946
