class Solution:
    def mySqrt(self, x: int) -> int:
        num = x
        while num * num > x:
            num = (num + x / num) // 2
        return int(num)


if __name__ == "__main__":
    print(Solution().mySqrt(4))  # 2
    print(Solution().mySqrt(8))  # 2
    print(Solution().mySqrt(1))  # 1
    print(Solution().mySqrt(9))  # 3
    print(Solution().mySqrt(5))  # 2
