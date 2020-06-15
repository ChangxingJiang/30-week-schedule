class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


if __name__ == "__main__":
    print(Solution().strStr("hello", "ll"))  # 2
    print(Solution().strStr("aaaaa", "bba"))  # -1
    print(Solution().strStr("hello", ""))  # 0
