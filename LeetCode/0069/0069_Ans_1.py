class Solution:
    def mySqrt(self, x: int) -> int:
        return int(pow(x, 0.5))


if __name__ == "__main__":
    print(Solution().mySqrt(4))  # 2
    print(Solution().mySqrt(8))  # 2
