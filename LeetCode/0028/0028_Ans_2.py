class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)

        # 处理长度为0的情况
        if needle_len == 0:
            return 0

        # 循环处理字符串
        j = 0
        i = 0
        while i < len(haystack):
            c = haystack[i]
            if c == needle[j]:
                if j == needle_len - 1:
                    return i - j
                else:
                    j += 1
                i += 1
            else:
                i = i - j + 1
                j = 0
        return -1


if __name__ == "__main__":
    print(Solution().strStr("hello", "ll"))  # 2
    print(Solution().strStr("aaaaa", "bba"))  # -1
    print(Solution().strStr("hello", ""))  # 0
    print(Solution().strStr("mississippi", "issip"))  # 4
