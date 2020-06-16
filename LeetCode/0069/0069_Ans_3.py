class Solution:
    def mySqrt(self, x: int) -> int:
        def find(a, b):
            if b - a <= 1:
                # print("R:", a, b)
                return a
            c = int((a + b) / 2)
            # print("C:", a, b, c, c * c > x)
            if c * c > x:
                return find(a, c)
            else:
                return find(c, b)
        return find(0, x + 1)


if __name__ == "__main__":
    print(Solution().mySqrt(4))  # 2
    print(Solution().mySqrt(8))  # 2
    print(Solution().mySqrt(1))  # 1
    print(Solution().mySqrt(9))  # 3
