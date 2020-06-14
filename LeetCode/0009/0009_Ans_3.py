class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)

        a = 0
        b = len(s) - 1
        while a <= b:
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(-121))
    print(Solution().isPalindrome(10))
