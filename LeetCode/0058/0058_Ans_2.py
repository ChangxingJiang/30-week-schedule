class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(" ")
        if s:
            return len(s.split(" ")[-1])
        else:
            return 0


if __name__ == "__main__":
    print(Solution().lengthOfLastWord("Hello World"))  # 5
    print(Solution().lengthOfLastWord("a "))  # 1
    print(Solution().lengthOfLastWord(" "))  # 0
    print(Solution().lengthOfLastWord(""))  # 0
