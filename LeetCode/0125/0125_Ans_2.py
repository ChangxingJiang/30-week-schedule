class Solution:
    def isPalindrome(self, s: str) -> bool:
        index_1 = 0
        index_2 = len(s) - 1
        while index_1 < index_2:
            if not s[index_1].lower().isalnum():
                index_1 += 1
                continue
            if not s[index_2].lower().isalnum():
                index_2 -= 1
                continue
            if s[index_1].lower() == s[index_2].lower():
                index_1 += 1
                index_2 -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))
