class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = abs(x)
            pre = -1
        else:
            pre = 1

        ans = 0
        while x > 0:
            ans = ans * 10 + x % 10
            x //= 10

        if -2147483648 < ans < 2147483647:
            return pre * ans
        else:
            return 0


if __name__ == "__main__":
    print(Solution().reverse(123))  # 321
    print(Solution().reverse(-123))  # -321
    print(Solution().reverse(120))  # (0)21
