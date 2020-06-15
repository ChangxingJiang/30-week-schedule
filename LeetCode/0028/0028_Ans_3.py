class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_h = len(haystack)
        len_n = len(needle)
        for i in range(len_h - len_n + 1):
            if haystack[i: i + len_n] == needle:
                return i
        return -1


if __name__ == "__main__":
    print(Solution().strStr("hello", "ll"))  # 2
    print(Solution().strStr("aaaaa", "bba"))  # -1
    print(Solution().strStr("hello", ""))  # 0
    print(Solution().strStr("mississippi", "issip"))  # 4
