class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        s = a + b
        s = bin(s)
        return str(s).replace("0b", "")


if __name__ == "__main__":
    print(Solution().addBinary("11", "1"))  # 100
    print(Solution().addBinary("1010", "1011"))  # 10101
