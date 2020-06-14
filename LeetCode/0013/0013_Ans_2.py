class Solution:
    def romanToInt(self, s: str) -> int:

        number = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        o = 0  # 上一个字符
        ans = 0  # 数值总计
        for c in s:
            n = number[c]
            if o < n:
                ans += n - 2 * o
            else:
                ans += n
            o = n
        return ans


if __name__ == "__main__":
    print(Solution().romanToInt("III"))  # 3
    print(Solution().romanToInt("IV"))  # 4
    print(Solution().romanToInt("IX"))  # 9
    print(Solution().romanToInt("LVIII"))  # 58
    print(Solution().romanToInt("MCMXCIV"))  # 1994
