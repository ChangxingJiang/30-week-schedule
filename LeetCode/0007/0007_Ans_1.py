class Solution:
    def reverse(self, x: int) -> int:
        l = [c for c in str(x).replace("-", "")]
        l.reverse()
        ans = int("".join(l))
        if -pow(2, 31) < ans < pow(2, 31) - 1:
            if x >= 0:
                return ans
            else:
                return -ans
        else:
            return 0


if __name__ == "__main__":
    print(Solution().reverse(123))  # 321
    print(Solution().reverse(-123))  # -321
    print(Solution().reverse(120))  # (0)21
