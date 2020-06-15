class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for w in s.split(" ")[::-1]:
            len_w = len(w)
            if len_w != 0:
                return len_w
        return 0


if __name__ == "__main__":
    print(Solution().lengthOfLastWord("Hello World"))  # 5
    print(Solution().lengthOfLastWord("a "))  # 1
    print(Solution().lengthOfLastWord(" "))  # 0
    print(Solution().lengthOfLastWord(""))  # 0
