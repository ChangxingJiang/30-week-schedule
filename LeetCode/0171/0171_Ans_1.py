class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans += (ord(s[-(i + 1)]) - 64) * pow(26, i)
        return ans


if __name__ == "__main__":
    print(Solution().titleToNumber("A"))  # 1
    print(Solution().titleToNumber("AB"))  # 28
    print(Solution().titleToNumber("ZY"))  # 701
