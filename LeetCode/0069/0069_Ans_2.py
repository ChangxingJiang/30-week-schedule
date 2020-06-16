class Solution:
    def mySqrt(self, x: int) -> int:
        num = 0
        for i in range(1, x + 1):
            if i * i > x:
                return num
            num = i
        return num


if __name__ == "__main__":
    print(Solution().mySqrt(4))  # 2
    print(Solution().mySqrt(8))  # 2
    print(Solution().mySqrt(1))  # 1
